#!/usr/bin/env python3
"""
lidar-bridge.py — LD06/LD19 LiDAR to MAVLink DISTANCE_SENSOR bridge.

Reads the LD06 on a serial port, decodes its 47-byte frames, and emits
DISTANCE_SENSOR (msgid 132) into mavlink-router on localhost. The router
forwards it to every attached GCS endpoint on the mesh.

    python3 /opt/nucleus/drone/lidar-bridge.py
    python3 /opt/nucleus/drone/lidar-bridge.py --port /dev/ttyUSB0 --baud 230400

Config is read from /etc/nucleus/mesh.conf (LIDAR_SERIAL, LIDAR_BAUD,
LIDAR_ORIENTATION, MAVLINK_UDP_PORT) and overridden by CLI flags.

LD06 frame format, 47 bytes, little-endian:
    0       header       0x54
    1       ver_len      0x2C  (0x2 = ver, 0xC = 12 points)
    2-3     speed        deg/s
    4-5     start_angle  centi-degrees
    6-41    12 x point   uint16 distance_mm + uint8 intensity
    42-43   end_angle    centi-degrees
    44-45   timestamp    ms, wraps at 30000
    46      crc8

The sensor is on a CP2102 USB bridge that drops out intermittently, so the
serial port is reopened on any error rather than exiting.
"""

import argparse
import os
import struct
import sys
import time

try:
    import serial
except ImportError:
    sys.exit("pyserial missing: sudo apt install python3-serial")

# Must be set before pymavlink is imported. Without it pymavlink builds
# MAVLink1 frames (0xFE start byte); the flight controller and mavlink-router
# both speak MAVLink2 (0xFD), so the GCS would see a mismatched dialect.
os.environ["MAVLINK20"] = "1"

try:
    from pymavlink import mavutil
except ImportError:
    sys.exit("pymavlink missing: pip install pymavlink")

MESH_CONF = "/etc/nucleus/mesh.conf"

DEFAULT_PORT = "/dev/ttyUSB0"
DEFAULT_BAUD = 230400
DEFAULT_UDP_PORT = 14550
DEFAULT_ORIENTATION = 25          # MAV_SENSOR_ROTATION_PITCH_270 (downward)

HEADER = 0x54
VER_LEN = 0x2C
FRAME_LEN = 47
POINTS = 12

# LD06 rated range is 0.02-12 m. DISTANCE_SENSOR is in centimetres.
MIN_CM = 2
MAX_CM = 1200

SEND_HZ = 10.0

# CRC8 table from the LD06 datasheet (poly 0x4D, init 0x00).
CRC_TABLE = [
    0x00, 0x4d, 0x9a, 0xd7, 0x79, 0x34, 0xe3, 0xae, 0xf2, 0xbf, 0x68, 0x25,
    0x8b, 0xc6, 0x11, 0x5c, 0xa9, 0xe4, 0x33, 0x7e, 0xd0, 0x9d, 0x4a, 0x07,
    0x5b, 0x16, 0xc1, 0x8c, 0x22, 0x6f, 0xb8, 0xf5, 0x1f, 0x52, 0x85, 0xc8,
    0x66, 0x2b, 0xfc, 0xb1, 0xed, 0xa0, 0x77, 0x3a, 0x94, 0xd9, 0x0e, 0x43,
    0xb6, 0xfb, 0x2c, 0x61, 0xcf, 0x82, 0x55, 0x18, 0x44, 0x09, 0xde, 0x93,
    0x3d, 0x70, 0xa7, 0xea, 0x3e, 0x73, 0xa4, 0xe9, 0x47, 0x0a, 0xdd, 0x90,
    0xcc, 0x81, 0x56, 0x1b, 0xb5, 0xf8, 0x2f, 0x62, 0x97, 0xda, 0x0d, 0x40,
    0xee, 0xa3, 0x74, 0x39, 0x65, 0x28, 0xff, 0xb2, 0x1c, 0x51, 0x86, 0xcb,
    0x21, 0x6c, 0xbb, 0xf6, 0x58, 0x15, 0xc2, 0x8f, 0xd3, 0x9e, 0x49, 0x04,
    0xaa, 0xe7, 0x30, 0x7d, 0x88, 0xc5, 0x12, 0x5f, 0xf1, 0xbc, 0x6b, 0x26,
    0x7a, 0x37, 0xe0, 0xad, 0x03, 0x4e, 0x99, 0xd4, 0x7c, 0x31, 0xe6, 0xab,
    0x05, 0x48, 0x9f, 0xd2, 0x8e, 0xc3, 0x14, 0x59, 0xf7, 0xba, 0x6d, 0x20,
    0xd5, 0x98, 0x4f, 0x02, 0xac, 0xe1, 0x36, 0x7b, 0x27, 0x6a, 0xbd, 0xf0,
    0x5e, 0x13, 0xc4, 0x89, 0x63, 0x2e, 0xf9, 0xb4, 0x1a, 0x57, 0x80, 0xcd,
    0x91, 0xdc, 0x0b, 0x46, 0xe8, 0xa5, 0x72, 0x3f, 0xca, 0x87, 0x50, 0x1d,
    0xb3, 0xfe, 0x29, 0x64, 0x38, 0x75, 0xa2, 0xef, 0x41, 0x0c, 0xdb, 0x96,
    0x42, 0x0f, 0xd8, 0x95, 0x3b, 0x76, 0xa1, 0xec, 0xb0, 0xfd, 0x2a, 0x67,
    0xc9, 0x84, 0x53, 0x1e, 0xeb, 0xa6, 0x71, 0x3c, 0x92, 0xdf, 0x08, 0x45,
    0x19, 0x54, 0x83, 0xce, 0x60, 0x2d, 0xfa, 0xb7, 0x5d, 0x10, 0xc7, 0x8a,
    0x24, 0x69, 0xbe, 0xf3, 0xaf, 0xe2, 0x35, 0x78, 0xd6, 0x9b, 0x4c, 0x01,
    0xf4, 0xb9, 0x6e, 0x23, 0x8d, 0xc0, 0x17, 0x5a, 0x06, 0x4b, 0x9c, 0xd1,
    0x7f, 0x32, 0xe5, 0xa8,
]


def crc8(data):
    crc = 0
    for byte in data:
        crc = CRC_TABLE[(crc ^ byte) & 0xFF]
    return crc


def read_mesh_conf():
    """Pull LIDAR_* and MAVLINK_UDP_PORT out of mesh.conf if present."""
    conf = {}
    try:
        with open(MESH_CONF) as fh:
            for line in fh:
                line = line.strip()
                if not line or line.startswith("#") or "=" not in line:
                    continue
                key, val = line.split("=", 1)
                conf[key.strip()] = val.strip().strip('"').strip("'")
    except OSError:
        pass
    return conf


def decode_frame(frame):
    """Decode one 47-byte LD06 frame into (start_deg, end_deg, points).

    points is a list of (distance_mm, intensity). Returns None if the CRC
    fails, which happens on a partial read or a resync.
    """
    if len(frame) != FRAME_LEN:
        return None
    if crc8(frame[:-1]) != frame[-1]:
        return None

    start_angle = struct.unpack_from("<H", frame, 4)[0] / 100.0
    end_angle = struct.unpack_from("<H", frame, 42)[0] / 100.0

    points = []
    for i in range(POINTS):
        off = 6 + i * 3
        dist_mm = struct.unpack_from("<H", frame, off)[0]
        intensity = frame[off + 2]
        points.append((dist_mm, intensity))

    return start_angle, end_angle, points


def frames(ser):
    """Yield validated LD06 frames from an open serial port.

    Resyncs by scanning for the 0x54 0x2C header, so a mid-frame start or a
    dropped byte costs at most one frame.
    """
    buf = bytearray()
    while True:
        chunk = ser.read(FRAME_LEN)
        if not chunk:
            return                      # read timeout, let caller reopen
        buf.extend(chunk)

        while True:
            idx = -1
            for i in range(len(buf) - 1):
                if buf[i] == HEADER and buf[i + 1] == VER_LEN:
                    idx = i
                    break
            if idx < 0:
                if len(buf) > FRAME_LEN * 4:
                    del buf[:-1]        # keep last byte, header may span reads
                break

            if idx:
                del buf[:idx]
            if len(buf) < FRAME_LEN:
                break

            decoded = decode_frame(bytes(buf[:FRAME_LEN]))
            if decoded:
                del buf[:FRAME_LEN]
                yield decoded
            else:
                del buf[:2]             # bad CRC, skip header and rescan

        if len(buf) > FRAME_LEN * 16:
            del buf[:]


def min_distance_cm(points):
    """Smallest in-range reading from a frame, in centimetres.

    Zero distance means no return, and the LD06 reports 0xFFxx style values
    when it sees nothing, so both are filtered out by the range check.
    Intensity 0 is also discarded as an invalid sample.
    """
    best = None
    for dist_mm, intensity in points:
        if dist_mm == 0 or intensity == 0:
            continue
        cm = dist_mm / 10.0
        if cm < MIN_CM or cm > MAX_CM:
            continue
        if best is None or cm < best:
            best = cm
    return best


def run(port, baud, udp_port, orientation, verbose):
    """Open the MAVLink endpoint once, then stream until interrupted.

    mavlink-router runs a UDP server, so this connects outbound to it on
    localhost. source_system 1 matches the flight controller's sysid so the
    GCS files the reading under the same vehicle.
    """
    conn = mavutil.mavlink_connection(
        f"udpout:127.0.0.1:{udp_port}", source_system=1, source_component=194)
    print(f"MAVLink out: udpout:127.0.0.1:{udp_port} "
          f"(DISTANCE_SENSOR, orientation {orientation})", flush=True)

    interval = 1.0 / SEND_HZ
    next_send = 0.0
    sent = 0
    started = time.monotonic()

    while True:
        try:
            ser = serial.Serial(port, baud, timeout=1.0)
        except (OSError, serial.SerialException) as exc:
            # CP2102 dropouts land here. Wait and retry rather than dying,
            # so the bridge survives the sensor coming and going.
            print(f"open {port} failed: {exc} - retry in 2s", flush=True)
            time.sleep(2)
            continue

        print(f"opened {port} @ {baud}", flush=True)
        try:
            for _start, _end, points in frames(ser):
                now = time.monotonic()
                if now < next_send:
                    continue
                next_send = now + interval

                cm = min_distance_cm(points)
                if cm is None:
                    continue

                conn.mav.distance_sensor_send(
                    time_boot_ms=int((now - started) * 1000) & 0xFFFFFFFF,
                    min_distance=MIN_CM,
                    max_distance=MAX_CM,
                    current_distance=int(round(cm)),
                    type=mavutil.mavlink.MAV_DISTANCE_SENSOR_LASER,
                    id=0,
                    orientation=orientation,
                    covariance=0,
                )
                sent += 1
                if verbose:
                    print(f"DISTANCE_SENSOR {int(round(cm))} cm  (sent {sent})",
                          flush=True)
                elif sent % 100 == 0:
                    print(f"sent {sent} DISTANCE_SENSOR, last {int(round(cm))} cm",
                          flush=True)
        except (OSError, serial.SerialException) as exc:
            print(f"{port} read error: {exc} - reopening", flush=True)
        finally:
            try:
                ser.close()
            except Exception:
                pass

        time.sleep(0.5)


def main():
    conf = read_mesh_conf()

    parser = argparse.ArgumentParser(
        description="Bridge an LD06/LD19 LiDAR into the MAVLink stream.")
    parser.add_argument("--port", default=conf.get("LIDAR_SERIAL", DEFAULT_PORT),
                        help="LiDAR serial device")
    parser.add_argument("--baud", type=int,
                        default=int(conf.get("LIDAR_BAUD", DEFAULT_BAUD)),
                        help="LiDAR baud rate (LD06 is 230400)")
    parser.add_argument("--udp-port", type=int,
                        default=int(conf.get("MAVLINK_UDP_PORT",
                                             DEFAULT_UDP_PORT)),
                        help="mavlink-router UDP port on localhost")
    parser.add_argument("--orientation", type=int,
                        default=int(conf.get("LIDAR_ORIENTATION",
                                             DEFAULT_ORIENTATION)),
                        help="MAV_SENSOR_ROTATION value (25 = downward)")
    parser.add_argument("--verbose", action="store_true",
                        help="log every message instead of every 100th")
    args = parser.parse_args()

    try:
        run(args.port, args.baud, args.udp_port, args.orientation, args.verbose)
    except KeyboardInterrupt:
        print("stopped", flush=True)
        return 0


if __name__ == "__main__":
    sys.exit(main())
