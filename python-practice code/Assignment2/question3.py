# 4. Write a host discovery tool in python you will determine the gateway ip and the IP class 
# ...existing code...

import os
import socket
import struct

def get_gateway_ip():
    # Windows-specific method to get gateway IP
    route = os.popen("route print 0.0.0.0").read()
    for line in route.splitlines():
        if "0.0.0.0" in line:
            parts = line.split()
            if len(parts) >= 4:
                return parts[2]
    return None

def get_ip_class(ip):
    first_octet = int(ip.split('.')[0])
    if 1 <= first_octet <= 126:
        return "Class A"
    elif 128 <= first_octet <= 191:
        return "Class B"
    elif 192 <= first_octet <= 223:
        return "Class C"
    elif 224 <= first_octet <= 239:
        return "Class D (Multicast)"
    elif 240 <= first_octet <= 254:
        return "Class E (Experimental)"
    else:
        return "Unknown"

def host_discovery():
    gateway_ip = get_gateway_ip()
    if gateway_ip:
        ip_class = get_ip_class(gateway_ip)
        print(f"Gateway IP: {gateway_ip}")
        print(f"IP Class: {ip_class}")
    else:
        print("Could not determine gateway IP.")

if __name__ == "__main__":
    # ...existing code...
    print("\nHost Discovery Tool")
    host_discovery()