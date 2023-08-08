import nmap

def get_mac_address(ip_address):
    nm = nmap.PortScanner()
    nm.scan(hosts=ip_address, arguments='-sn -PR')

    for host in nm.all_hosts():
        if 'mac' in nm[host]['addresses']:
            return nm[host]['addresses']['mac']

    return None

# Example usage: get the MAC address of a client with IP address 192.168.1.100
ip_address = "192.168.0.108"
mac_address = get_mac_address(ip_address)
print(mac_address)
