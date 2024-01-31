Using a network card with monitoring mode turned on we could scan for beacon packets `802.11` and using these could identify which devices are the [Access points]

> [!abstract]- Code
>
> ```python
> from scapy.all import Dot11, sniff
> def handle_beacon(packet):
>     if packet.haslayer(Dot11) and (packet.type == 0 and packet.subtype == 8):
>         ssid = packet.info.decode("utf-8", errors="ignore")
>         print(f"SSID: {ssid}")
>
> def main():
>     iface = "WiFi"  # Change this to your Wi-Fi interface name (e.g., "Wi-Fi")
>     print(f"Sniffing on interface {iface}...")
>     # Use npf for npcap, or wpcap for winpcap
>     sniff(prn=handle_beacon, iface=iface, store=0)
> if __name__ == "__main__":
>     main()
> ```

This Idea is based on the fact that access points periodically transmit [beacon frames]. A Beacon frame is a type of management frame from the IEEE 802.11 protocol, these frames
