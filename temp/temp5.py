from scapy.all import ARP, Ether, srp

def get_mac_address(ip_address):
    arp_request = ARP(pdst=ip_address)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether / arp_request
    result = srp(packet, timeout=3, verbose=0)[0]

    if result:
        return result[0][1].hwsrc
    else:
        return None

# Example usage: get the MAC address of a client with IP address 192.168.1.100
ip_address = "192.168.0.108"
mac_address = get_mac_address(ip_address)
print(mac_address)
