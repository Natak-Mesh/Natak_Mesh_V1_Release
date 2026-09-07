# Drone Hardware

## Parts

### Matek H743-SLIM V2

Connected to the Pi over the PL011 UART on GPIO14/15 — header pins 8 and 10.

| Pi Zero 2 W | H743-SLIM |
|---|---|
| pin 8, GPIO14 (TXD) | `RX2` |
| pin 10, GPIO15 (RXD) | `TX2` |
| pin 6, GND | `GND` |

FC side is the `TX2`/`RX2` through-holes (USART2), which ArduPilot exposes as
`SERIAL3`. On the Pi the port is `/dev/ttyAMA0` at 921600 baud.

Bluetooth must be disabled to get access to these pins. The Bluetooth
controller claims the PL011 UART by default, so `/dev/ttyAMA0` does not exist
until `dtoverlay=disable-bt` is set in `/boot/firmware/config.txt`.

The FC runs 3.3V and GND off the Pi power pins.

### MicoAir MTF-01

![MicoAir MTF-01 wiring](mico-air-MTF-01-wiring.jpg)

Assumes the sensor is on the autopilot's Serial1 port. Any serial port can be
used.

| Parameter | Value | Meaning |
|---|---|---|
| `SERIAL1_BAUD` | `115` | 115200 |
| `SERIAL1_PROTOCOL` | `1` | MAVLink1 |
| `FLOW_TYPE` | `5` | MAVLink |
| `RNGFND1_TYPE` | `10` | MAVLink |

Reboot the autopilot to see the rangefinder parameters, then set:

| Parameter | Value | Meaning |
|---|---|---|
| `RNGFND1_MAX` | `8` | Maximum range 8m |
| `RNGFND1_MIN` | `0.01` | Minimum range |
| `RNGFND1_ORIENT` | `25` | Downward |

Once the sensor is active, the optical flow and range data show up on Mission
Planner's "Status" page — `opt_qua` and `rangefinder1` should have some value.

### LDRobot D500

Connected via USB to the companion computer.

## FC UART Allocation

Through-holes on the H743-SLIM are silkscreened with the STM32 UART number,
which is **not** the ArduPilot `SERIALn` number. Mapping below.

| Through-holes | STM32 UART | ArduPilot |
|------|------|------|
| `TX2` / `RX2` | USART2 | SERIAL3 |
| `TX7` / `RX7` | UART7 | SERIAL1 |
| `TX3` / `RX3` | USART3 | SERIAL4 |
| `TX4` / `RX4` | UART4 | SERIAL6 |

UART7 is the only port with `CTS7`/`RTS7` broken out.
