from scapy.all import ARP, Ether, srp


def get_mac(ip):
    arp = ARP(pdst=ip)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether / arp
    result = srp(packet, timeout=3, verbose=0)[0]
    return result[0][1].hwsrc


def get_connected_ap(device_ip, ap_ips):
    device_mac = get_mac(device_ip)

    for ap_ip in ap_ips:
        ap_mac = get_mac(ap_ip)
        if device_mac == ap_mac:
            return ap_ip

    return "Device not connected to any known AP."


# Example usage:
ap_ips = ["192.168.1.29", "192.168.1.98"]
device_ip = "192.168.1.165"
connected_ap = get_connected_ap(device_ip, ap_ips)
print(f"The device is connected to AP with IP: {connected_ap}")
