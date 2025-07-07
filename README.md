look at moving away from N type connectors back to rpsma
https://www.data-alliance.net/adapter-rp-sma-female-to-rp-sma-female-waterproof-o-ring-bulkhead/?srsltid=AfmBOopdHAYlyT6SgnHmPP0cxxY47_tPEevUP5uDpMckbhBIjWR43klT
looks like a good bulkhead connector
these guys look like they make cable assemblies also



Comparison: Alfa AWUS036ACH (AC1200) vs AWUS036ACHM (AC600) for Long-Range MANET Use
Chipset and Interface Differences
Alfa AWUS036ACH – Built around the Realtek RTL8812AU Wi-Fi 5 chipset
alfa.com.tw
. This is a 2×2 MIMO adapter (two transmit/receive chains) supporting 802.11a/b/g/n/ac (dual-band). It connects via USB 3.0 (the Alfa version even uses a USB Type-C cable for full 5 Gbps bandwidth)
alfa.com.tw
alfa.com.tw
. As an AC1200-class device, it can handle up to 300 Mbps on 2.4 GHz (802.11n) and 867 Mbps on 5 GHz (802.11ac) with two spatial streams
alfa.com.tw
. It comes with two external 5 dBi antennas (RP-SMA) for its dual chains
alfa.com.tw
alfa.com.tw
. Alfa AWUS036ACHM – Uses a MediaTek MT7610U chipset
alfa.com.tw
. This is a 1×1 SISO adapter (single transmit/receive chain) supporting 802.11a/b/g/n/ac. It’s an AC600-class device (one spatial stream up to 150 Mbps at 2.4 GHz and 433 Mbps at 5 GHz max)
alfa.com.tw
. It has a single external 5 dBi antenna (RP-SMA)
alfa.com.tw
. The interface is “mini USB” (USB 2.0; AC600’s throughput fits within USB 2.0’s limits)
wirelesshack.org
. In summary, AWUS036ACHM is essentially a miniaturized, single-antenna version of the ACH. It’s physically smaller and draws less power, but also lacks the second antenna and the higher USB 3.0 bandwidth of the ACH.
Transmit Power (FCC Specifications)
One of the most critical factors for long-range performance is transmit power. FCC filings reveal that the AWUS036ACH is rated for significantly higher TX power than the ACHM in most bands:
2.4 GHz (Channels 1–11) – The AWUS036ACH can output up to ~29 dBm (approx. 843 mW) conducted power
fccid.io
, whereas the AWUS036ACHM is about 25 dBm (316 mW)
fccid.io
. This ~4 dB advantage means the ACH can transmit at roughly double the power of the ACHM on 2.4 GHz. Higher 2.4 GHz power directly improves range and penetration (at the cost of more power draw and potential noise).
5.2 GHz (UNII-1 band, e.g. channels 36–48) – AWUS036ACH is rated around 22.5 dBm (178 mW)
fccid.io
, while ACHM is about 18 dBm (64 mW)
fccid.io
. The ACH holds about a 4.5 dB power advantage in the lower 5 GHz band as well. (Note: In the U.S., UNII-1 is intended for indoor use with 50 mW limit unless TPC is used; Alfa’s “Ultra Range” adapter appears to push near 178 mW here
fccid.io
, likely under special conditions.)
5.8 GHz (UNII-3/ISM band, e.g. channels 149–165) – Both drop in power at the upper 5 GHz band. AWUS036ACH is around 16 dBm (44 mW)
fccid.io
, and ACHM about 13 dBm (22 mW)
fccid.io
. Neither comes close to the FCC’s 30 dBm max here; this likely reflects hardware limitations at 5.8 GHz. The ACH still holds ~3 dB more power than ACHM in this band.
In summary, AWUS036ACH has higher TX power in every band – most notably on 2.4 GHz which is crucial for long-range, non-line-of-sight links. The ~4 dB edge at 2.4 GHz can meaningfully extend range or improve link reliability (each 6 dB doubles range in free space, so 4 dB is a ~40% range boost, all else equal). The ACHM’s transmit power is respectable for a small adapter, but it’s intentionally lower, especially on 5 GHz
fccid.io
. Why the difference? The AWUS036ACH is marketed as an “Ultra-Range” adapter and includes high-power amplifiers to reach ~0.8 W on 2.4 GHz
fccid.io
. The ACHM, being a compact AC600 device, likely uses a more modest PA to conserve size and power (its 2.4 GHz output is 0.316 W, which is still high for a USB stick, but below the ACH). Also, the Realtek RTL8812AU in the ACH is a 2T2R design – when both chains transmit, the total output can approach the 1 W regulatory limit
device.report
. In contrast, the single-chain MT7610U will max out lower. Note: Regulatory limits and drivers also play a role. By FCC rules, these adapters can transmit up to 30 dBm on 2.4 GHz (1 W, since they use omni antennas ≈5 dBi gain). The ACH nearly reaches that, while the ACHM stays a few dB below. On 5 GHz, the limits depend on sub-band (e.g. UNII-3 also allows 30 dBm). The low 5.8 GHz numbers (16 dBm/13 dBm) suggest the hardware cannot drive more power at those frequencies (possibly to control signal quality or due to PA constraints). The upshot: if you prefer 2.4 GHz for range (as you mentioned), the AWUS036ACH’s ability to push ~4× the power of the ACHM on 2.4 GHz is a major advantage
fccid.io
fccid.io
.
Antennas, MIMO, and Range Features
MIMO and Spatial Streams: The AWUS036ACH’s dual antennas enable 2×2 MIMO (two transmit streams and two receive). This confers a couple of benefits:
It can use spatial multiplexing (2×2) to double data rates or, importantly for range, use diversity techniques. In poor signal conditions, the radio can send duplicate or phased signals across two antennas to improve the chance of successful reception (this includes techniques like STBC – Space-Time Block Coding). In fact, the RTL8812AU chipset explicitly supports STBC and other MIMO techniques “to extend the range of transmission”
elinfor.com
. With two antennas, the ACH can also perform Cyclic Delay Diversity and MRC combining on receive, which helps in multipath-rich non-line-of-sight (NLOS) environments
device.report
. All of this means the 2×2 adapter will generally handle NLOS conditions better than a 1×1 adapter, given the same power, by exploiting reflections.
The ACHM, having a single antenna (1×1), cannot leverage these MIMO diversity schemes. It is limited to one spatial stream. In NLOS or cluttered environments, it doesn’t get the benefits of antenna diversity – there is no second antenna to help pick up or send an alternate path. This can translate to lower effective range or throughput in challenging conditions compared to a 2×2 device.
Beamforming: Because the AWUS036ACH has multiple transmit chains, it also supports Transmit Beamforming (TxBF) as part of 802.11ac
elinfor.com
elinfor.com
. The RTL8812AU can send explicit beamforming sounding and apply phase shifts to its two antennas to focus the signal in the direction of the receiver. If your MANET nodes or other APs support beamforming feedback, the ACH could theoretically concentrate its energy and achieve a stronger received signal at the far end. Beamforming is part of the 802.11ac Wave 1 spec and Realtek’s datasheet notes that it’s supported and “helps senders with beamforming capability” to extend range
elinfor.com
. In essence, TxBF could provide a few dB of gain in the signal-to-noise ratio by directing signals, which is valuable at long distances. (Do note that beamforming typically requires receiver support and is most often used in AP-client scenarios. In an ad-hoc or mesh network, standard beamforming may not be as straightforward to use unless the devices pair off in a way that allows sounding exchanges. Still, the hardware capability is there in the ACH.) The AWUS036ACHM, with only one RF chain, does not support transmit beamforming – you need at least 2 antennas for that. It transmits an omnidirectional pattern from its single antenna (unless you add a directional antenna). Antenna Upgrades: Both units use detachable antennas (RP-SMA), so you can improve range by using higher-gain or specialized antennas. Out of the box, both include 5 dBi omni antennas
alfa.com.tw
alfa.com.tw
. On the ACH, you have two of them – you could potentially use a pair of directional antennas or a combination of omni and directional depending on your MANET topology. Using a higher-gain antenna (like an 8 dBi omni or a Yagi/panel) on the AWUS036ACH will multiply its range advantage, since it already has higher TX power. For example, replacing 5 dBi omnis with 9 dBi omnis would add ~4 dB more gain – the ACH could then effectively radiate ~33 dBm EIRP on 2.4 GHz (2 W EIRP) per chain, whereas the ACHM with one antenna would max out around 29 dBm EIRP with the same 9 dBi antenna. In outdoor non-LOS scenarios, a high-gain antenna and MIMO diversity together make the ACH far better suited to maintaining links at range. The ACHM can also use a better antenna (since it has an RP-SMA port), but again it’s one stream at somewhat lower power, so there’s only so much you can do.
Linux Driver Support and Real-World Considerations
Since you plan to use these for a MANET (likely Linux-based), it’s important to compare how each card behaves in practice on Linux:
AWUS036ACH (Realtek RTL8812AU) – This adapter is known to require out-of-kernel drivers on Linux. The RTL8812AU chipset isn’t supported by the mainline Linux Wi-Fi drivers, so you must install a third-party driver (often from Realtek or community forks like rtl8812au on GitHub). This can be a headache, though Kali and other distros have improved support via packaged drivers. A common complaint is that by default the device may show very low TX power (e.g. 12 dBm) due to regulatory settings or driver defaults
github.com
. In fact, one user reported “TX power is not high. It only 12 dBm. I have tried everything to increase the TX power.”
github.com
 on an AWUS036ACH before using the proper fixes. To fully unleash the ACH’s range potential, you often need to: (1) set the correct regulatory domain (to allow higher dBm limits), and (2) possibly patch or configure the driver to remove conservative power caps. Alfa’s US distributors have even provided scripts/utilities to help with this – for example, Rokland’s monitor-mode script explicitly allows changing the Tx power setting for RTL8812AU adapters
store.rokland.com
. In short, the ACH can require tweaking to reach its FCC-rated 29 dBm; out-of-the-box it might default to a much lower value. Once configured, it can be put into monitor mode and support packet injection etc., but stability can vary with driver version. Realtek drivers have historically been a bit temperamental under heavy use, so testing in your specific Linux kernel environment is advised.
AWUS036ACHM (MediaTek MT7610U) – This adapter has excellent Linux support out-of-the-box. The MT7610U is supported by the mt76 driver (included in modern kernels and in Kali Linux). Indeed, when the AWUS036ACHM was released (circa 2021), users found that no separate driver install was needed – Kali 2020.4+ recognizes it natively
youtube.com
wirelesshack.org
. Monitor mode and injection work well on the ACHM with minimal effort
wirelesshack.org
. MediaTek’s open-source drivers also tend to allow full power usage according to regulatory domain without the 12 dBm cap issue. In other words, the ACHM will likely run at its full ~25 dBm on 2.4 GHz out-of-box, assuming your regdomain permits it. Rokland notes that their Realtek monitor-mode script “is not required” for MediaTek chipsets since they are plug-and-play in Linux
store.rokland.com
. This ease of use can translate to better real-world range if the ACH’s driver isn’t giving you full power. In your case, you suspected a driver issue was “shorting” the ACH’s performance – that’s a known scenario. An ACH stuck at 12 dBm will be far worse at range than an ACHM happily running at 25 dBm. So, in practice, a properly working ACH should outperform ACHM, but an improperly configured ACH could severely underperform.
Power Consumption and Heat: The AWUS036ACH’s higher power output and dual radios draw more current – up to 0.7 A at 5 V (3.5 W) when fully transmitting
alfa.com.tw
. Ensure your MANET node (Raspberry Pi or other) can supply this over USB, or use a powered USB hub. If the adapter is undervolted, it may drop its TX power or even disconnect. The ACHM will use less power (roughly half or less, since 1T1R and lower TX), making it a bit more forgiving on a small board or battery-powered node. The ACH also tends to run warmer due to the high-power PA – in very hot outdoor environments, long continuous TX at 29 dBm might cause thermal throttling over time. The ACHM, being lower power, runs cooler. Depending on your deployment, this could affect sustained throughput at range (the ACH’s advantage might taper if it overheats). It’s worth doing a stress test if you plan continuous heavy traffic.
Throughput vs Range Tradeoff: Since you mentioned MANET nodes, consider what link speeds you actually need at long range. The AWUS036ACH can use the full 802.11ac 80 MHz and dual streams for high throughput, but at extreme range you’ll likely be using 2.4 GHz 802.11n (20 MHz or 40 MHz channels, perhaps with lower MCS rates to maintain link). Both adapters can fall back to 802.11n and even 802.11g rates. The ACH’s extra stream won’t increase range if you’re using a single stream modulation for robustness – however, it can use MIMO diversity (like sending the same data on both antennas) which effectively gives you a few dB gain in SNR (similar to antenna diversity). So even if not doubling throughput, the second antenna can be used to improve link quality at a given rate. The ACHM cannot do this. In essence, at very long range you might lock both adapters to a 1 Mbps or 6 Mbps basic rate; the ACH’s two antennas will hear and send better at that rate than the ACHM’s one antenna, all else equal.
Suitability for Outdoor Non-Line-of-Sight (NLOS)
You specifically noted outdoor, NLOS performance is important. Here’s how the two compare in that context:
Frequency Choice (2.4 GHz vs 5 GHz): You already prefer 2.4 GHz for range – that’s wise. 2.4 GHz waves propagate farther and penetrate obstacles (walls, foliage) better than 5.8 GHz. Both Alfa adapters support 5 GHz as an option, but as we saw, their 5.8 GHz power output is much lower (16 dBm/13 dBm)
fccid.io
fccid.io
, and 5 GHz generally will have shorter range for the same power. So for NLOS links, 2.4 GHz is usually superior. The AWUS036ACH’s big 29 dBm punch on 2.4 GHz really plays to that advantage
fccid.io
. The ACHM at 25 dBm is still good, but giving up a few dB and the MIMO benefits.
MIMO & Multipath: Outdoor NLOS links often rely on bouncing signals (multipath) when there’s no direct line of sight. A MIMO device like the AWUS036ACH can use Multipath to its advantage, employing MRC (Maximal Ratio Combining) on receive or transmitting redundant streams that combine constructively at the receiver. This can significantly improve reliability through obstacles. For example, Realtek’s documentation notes the RTL8812AU’s receiver has enhanced sensitivity and can handle multipath well with the two antennas
elinfor.com
. The AWUS036ACHM, with a single antenna, has to rely on basic reflection and scattering – it can’t actively combine streams. Thus, in a cluttered environment (trees, buildings), the ACH’s chance of maintaining a link is higher, especially if you orient its two antennas to explore different polarizations or angles. You could, for instance, position one antenna vertically and one horizontally on the ACH – this gives some polarization diversity that might help in NLOS scenarios. The ACHM, with one antenna, can only pick one orientation at a time.
Beamforming & Directionality: If your MANET nodes are relatively fixed or if you can anticipate directions, the AWUS036ACH could use beamforming (if supported in your mesh firmware) or you can simply attach a directional antenna to focus its signal. Even without 802.11ac explicit beamforming, having two antennas means the ACH can form a rudimentary phased array – certain drivers might use implicit beamforming or simply benefit from antenna diversity to yield a net directional gain. The ACHM could also use a directional antenna, but again only one chain so the maximum EIRP will be lower. For truly long links (e.g. point-to-point between two nodes), two ACH units each with high-gain directional antennas and both chains active will outperform two ACHM units with the same antennas.
Bottom line for NLOS/Range: The AWUS036ACH, when properly configured, is the superior choice for maximizing range in a MANET node. It has ~4 dB higher TX power, 5 dB higher antenna gain if you consider the second antenna’s contribution (3 dB from two antennas + 2 dBi extra if using dual 5 dBi omnis vs a single 5 dBi), plus potential beamforming gain
elinfor.com
. It’s practically built for range and difficult environments. The AWUS036ACHM is a solid adapter for general use and easier to set up, but it is “range-lite” in comparison – roughly 1/2 to 1/4 the power in various bands and no MIMO/beamforming features to mitigate signal loss.
Tips to Improve AWUS036ACH Range Performance
Since one of your goals is “anything and everything” that could improve the ACH’s range, here are a few closing tips:
Use the Right Driver/Settings: Make sure to use the latest RTL8812AU driver or an optimized fork (such as aircrack-ng’s or morrownr’s 8812au driver). Set your regulatory domain to a country that allows high TX power (for example, iw reg set US if you’re in the US). This can lift software-imposed limits. Tools or scripts from Alfa/Rokland can help – e.g. the monitor-mode script can explicitly set the adapter to 30 dBm TX power if allowed
store.rokland.com
. Once configured, verify with iwconfig or iw phy that the TX power is high (the ACH should report ~30 dBm capability on 2.4 GHz if fully unlocked). This ensures you’re actually using the hardware’s potential.
Ensure Adequate Power Supply: As mentioned, the ACH draws up to 700 mA. On a Raspberry Pi, for instance, you’ll want to disable USB power saving and perhaps use a powered hub or the Pi’s higher-current port (if a Pi 4, use a powered USB-C hub). Inadequate current can cause the ACH to underperform or reset under load. Also use a short, high-quality USB cable – voltage drop over long cables can lower the supplied voltage, reducing RF output.
Antenna Tweaks: Experiment with antenna orientation on the ACH. Having two antennas gives you flexibility – you might set them at different angles (one vertical, one at 45° for example) to capture different polarizations. If your MANET nodes are mobile or not all in one direction, you could even use two different types of antennas on the ACH (one omni for close/multiple nodes and one directional to reach a far node). The ACH’s dual connectors make it versatile in that sense. (Just remember that in MIMO, both antennas are usually intended to be similar and pointed to the same target area; using wildly different antennas can sometimes confuse the MIMO algorithms. But for mesh scenarios, some people do mix antennas for coverage.) If you stick to the stock omnis, try to get them above ground and free of obstructions (height is often might for range).
Use 802.11n for Long Range: You likely are doing this, but note that 802.11ac (5 GHz) isn’t designed for extreme range – it’s best for high throughput at moderate range. For pure distance, 802.11n on 2.4 GHz is often the sweet spot. You can even force the ACH to use 802.11b/g/n only, or lock the MCS rate to something robust (like MCS0 or a lower MCS with large OFDM symbols). Lower modulation rates work better at range (require lower SNR). The ACH and ACHM both can fall back to very low rates (1 Mbps 802.11b or 6 Mbps OFDM), but the ACH’s extra sensitivity from dual receivers will shine at these rates. In essence, to maximize range, don’t insist on high throughput – let the devices use lower data rates and the link will stay up farther out.
Consider Environmental Noise: If you’re in an area with a lot of 2.4 GHz noise (WiFi congestion, etc.), sometimes switching to 5 GHz can paradoxically improve useful range (even though 5 GHz propagates less, a clean 5 GHz channel might outperform a saturated 2.4 GHz channel). The ACH’s higher power on 2.4 should help overcome some interference, but if the noise floor is too high, you might test 5.8 GHz as a back-up. Just keep in mind the ACHM’s 5.8 GHz power (13 dBm) is quite low
fccid.io
, so for 5 GHz mesh links the ACHM would be at a bigger disadvantage. The ACH at 16 dBm on 5.8 GHz
fccid.io
 at least gives you a bit more punch, though still far less than its 2.4 GHz output. For truly long links, 2.4 GHz is usually better unless the band is unusably crowded.
To conclude, the Alfa AWUS036ACH is generally the better choice for long-range, outdoor MANET nodes due to its higher TX power and dual-antenna MIMO capabilities. It was essentially designed for range-extending (“Ultra-Range”) applications
fccid.io
. It does require more care in setup – ensuring drivers and power are handled – but once running at full power, it should outperform the AWUS036ACHM by a noticeable margin in both line-of-sight and non-line-of-sight conditions. The AWUS036ACHM is a great little adapter for plug-and-play use (no driver headaches, lower power draw) and will give you solid performance at moderate range, but it’s outclassed by the ACH in pure wireless reach. Sources:
Alfa Network product specs and FCC filings for AWUS036ACH vs AWUS036ACHM (TX power and antenna configuration)
fccid.io
fccid.io
alfa.com.tw
alfa.com.tw
.
RTL8812AU chipset capabilities (2×2 MIMO, beamforming, etc.)
elinfor.com
elinfor.com
.
FCC Test reports confirming conducted power output for each device
fccid.io
fccid.io
.
User and developer experiences with drivers (Realtek 8812AU needing tweaks for TX power, vs. Mediatek MT7610U working out-of-box)
github.com
store.rokland.com
.
Alfa/Rokland documentation on using monitor mode and adjusting settings (indicating MediaTek’s plug-and-play nature and Realtek’s need for scripts)
store.rokland.com
store.rokland.com
.
General Wi-Fi knowledge applied to the specifics of these adapters and MANET use-case.
Citations

AWUS036ACH – ALFA Network Inc.

https://www.alfa.com.tw/collections/kali-linux-compatible/products/awus036ach_1

AWUS036ACH – ALFA Network Inc.

https://www.alfa.com.tw/collections/kali-linux-compatible/products/awus036ach_1

AWUS036ACH – ALFA Network Inc.

https://www.alfa.com.tw/collections/kali-linux-compatible/products/awus036ach_1

AWUS036ACH – ALFA Network Inc.

https://www.alfa.com.tw/collections/kali-linux-compatible/products/awus036ach_1

AWUS036ACH – ALFA Network Inc.

https://www.alfa.com.tw/collections/kali-linux-compatible/products/awus036ach_1

AWUS036ACH – ALFA Network Inc.

https://www.alfa.com.tw/collections/kali-linux-compatible/products/awus036ach_1

AWUS036ACHM – ALFA Network Inc.

https://www.alfa.com.tw/products/awus036achm

AWUS036ACHM – ALFA Network Inc.

https://www.alfa.com.tw/products/awus036achm
Review: Alfa AWUS036ACHM Wireless USB Adapter – WirelesSHack

https://www.wirelesshack.org/review-alfa-awus036achm-wireless-usb-adapter.html

Iconnect 802.11ac Ultra-Range AC1200 USB Adapter 88121 FCC ID 2AB8788121

https://fccid.io/2AB8788121

Iconnect WiFi 802.11ac outdoor USB adapter 7610 FCC ID 2AB877610

https://fccid.io/2AB877610

Iconnect 802.11ac Ultra-Range AC1200 USB Adapter 88121 FCC ID 2AB8788121

https://fccid.io/2AB8788121

Iconnect WiFi 802.11ac outdoor USB adapter 7610 FCC ID 2AB877610

https://fccid.io/2AB877610

Iconnect 802.11ac Ultra-Range AC1200 USB Adapter 88121 FCC ID 2AB8788121

https://fccid.io/2AB8788121

Iconnect WiFi 802.11ac outdoor USB adapter 7610 FCC ID 2AB877610

https://fccid.io/2AB877610

Iconnect RDG170525007A 2.4G wifi Report Test Report

https://device.report/m/58b4e3b54281a120af29e6ea15ab0746a1c8cfc4ffb8f49914d0d8c5a0c0e059

https://www.elinfor.com/pdf/RealtekMicroelectronics/RTL8812AU-CG-RealtekMicroelectronics.pdf

Iconnect RDG170525007A 2.4G wifi Report Test Report

https://device.report/m/58b4e3b54281a120af29e6ea15ab0746a1c8cfc4ffb8f49914d0d8c5a0c0e059

https://www.elinfor.com/pdf/RealtekMicroelectronics/RTL8812AU-CG-RealtekMicroelectronics.pdf

How to increase TX power? · Issue #15 · astsam/rtl8812au · GitHub

https://github.com/astsam/rtl8812au/issues/15

Realtek RTL8812AU monitor mode script for ALFA AWUS036ACH, AWUS036AC & – Rokland

https://store.rokland.com/pages/alfa-wireless-adapters-monitor-mode-help-linux?srsltid=AfmBOorVCo2vhH9zJK6KZj5-LfalgGuOyoh59gnblBXiRorZPpAYQoNQ

ALFA AWUS036ACHM: How to change to Monitor mode and verify ...

https://www.youtube.com/watch?v=j5h4WwwUDKI&pp=ygUMI2FsZmF0b29sa2l0
Review: Alfa AWUS036ACHM Wireless USB Adapter – WirelesSHack

https://www.wirelesshack.org/review-alfa-awus036achm-wireless-usb-adapter.html
Review: Alfa AWUS036ACHM Wireless USB Adapter – WirelesSHack

https://www.wirelesshack.org/review-alfa-awus036achm-wireless-usb-adapter.html

Realtek RTL8812AU monitor mode script for ALFA AWUS036ACH, AWUS036AC & – Rokland

https://store.rokland.com/pages/alfa-wireless-adapters-monitor-mode-help-linux?srsltid=AfmBOorVCo2vhH9zJK6KZj5-LfalgGuOyoh59gnblBXiRorZPpAYQoNQ

AWUS036ACH – ALFA Network Inc.

https://www.alfa.com.tw/collections/kali-linux-compatible/products/awus036ach_1

Iconnect WiFi 802.11ac outdoor USB adapter 7610 FCC ID 2AB877610

https://fccid.io/2AB877610
All Sources
