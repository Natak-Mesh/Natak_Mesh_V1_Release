look at moving away from N type connectors back to rpsma
https://www.data-alliance.net/adapter-rp-sma-female-to-rp-sma-female-waterproof-o-ring-bulkhead/?srsltid=AfmBOopdHAYlyT6SgnHmPP0cxxY47_tPEevUP5uDpMckbhBIjWR43klT
looks like a good bulkhead connector
these guys look like they make cable assemblies also



Technical Comparison: Alfa AWUS036ACH vs AWUS036ACHM for MANET Applications

Overview

This document provides a detailed technical comparison between the Alfa AWUS036ACH and Alfa AWUS036ACHM wireless adapters, focusing on their suitability for outdoor Mobile Ad-hoc Network (MANET) deployments. It includes an analysis of FCC filings, chipset capabilities, Linux driver support, and performance-enhancing features.

1. Chipset and Hardware Differences

Feature

AWUS036ACH

AWUS036ACHM

Chipset

Realtek RTL8812AU

MediaTek MT7610U

MIMO

2×2 (dual stream)

1×1 (single stream)

USB Interface

USB 3.0 (Type-C)

USB 2.0 (mini USB)

Antenna

2× 5 dBi RP-SMA (detachable)

1× 5 dBi RP-SMA (detachable)

Max Data Rate

300 Mbps (2.4 GHz) / 867 Mbps (5 GHz)

150 Mbps (2.4 GHz) / 433 Mbps (5 GHz)

The AWUS036ACH supports dual-stream MIMO and beamforming features, whereas the AWUS036ACHM is a compact, single-stream adapter.

2. FCC Transmit Power Analysis

Band

AWUS036ACH TX Power

AWUS036ACHM TX Power

2.4 GHz (Ch 1–11)

~29 dBm (~843 mW)

~25 dBm (~316 mW)

5.2 GHz (UNII-1)

~22.5 dBm (~178 mW)

~18 dBm (~64 mW)

5.8 GHz (UNII-3)

~16 dBm (~40 mW)

~13 dBm (~20 mW)

Key Insight: The AWUS036ACH consistently offers 3–4 dB more power across bands, with a significant edge at 2.4 GHz, critical for range and NLOS scenarios.

3. Antenna Configuration and Range Features

AWUS036ACH

Dual antennas enable 2×2 MIMO and STBC for multipath resilience.

Supports Explicit Beamforming under 802.11ac.

Flexible antenna setup (omni + directional combinations possible).

AWUS036ACHM

Single antenna limits it to SISO.

No beamforming support.

Advantage: The ACH’s dual antenna system enhances NLOS performance by leveraging multipath reflections and diversity gains.

4. Linux Driver Support

Feature

AWUS036ACH

AWUS036ACHM

Driver

rtl8812au (3rd party required)

mt76 (in-kernel)

Plug-and-Play

No

Yes

TX Power Adjustments

Often required (scripts/patched drivers)

Native full power support

Insight: The ACHM works out-of-box on modern Linux (Kali, Ubuntu), while the ACH may require configuration to unlock full TX power.

5. Performance Optimization for AWUS036ACH

Driver Tweaks: Install latest rtl8812au drivers, set regulatory domain (e.g., iw reg set US).

Power Supply: Use high-quality USB 3.0 cable; consider powered hub for Raspberry Pi nodes.

Antenna Strategy: Experiment with orientation; consider high-gain directional antennas.

Frequency Band: Prefer 2.4 GHz for long-range; 5 GHz as backup in low-noise environments.

Throughput Settings: Force lower MCS rates or 802.11n for better stability at extreme ranges.

6. Summary Table

Attribute

AWUS036ACH

AWUS036ACHM

TX Power (2.4 GHz)

~29 dBm

~25 dBm

MIMO

2×2

1×1

Beamforming

Yes

No

Linux Ease

Moderate (needs driver/config)

Excellent (plug-and-play)

Power Draw

~3.5 W

~1.5 W

Best For

Long-range, NLOS MANET links

Simpler, moderate range nodes

7. Recommendation

The AWUS036ACH is the superior choice for MANET nodes where maximum range, NLOS performance, and multipath resilience are critical. Its higher TX power, dual antennas, and MIMO/beamforming capabilities make it ideal for challenging outdoor deployments.

The AWUS036ACHM is better suited for scenarios where ease of setup, lower power consumption, and compactness are more important than ultimate range.

8. References (FCC & Datasheets)

FCC ID AWUS036ACH: 2AB8776101

FCC ID AWUS036ACHM: 2AB8776131

Realtek RTL8812AU Datasheet

Alfa Network Product Pages

Linux Kernel mt76 Driver Documentation


