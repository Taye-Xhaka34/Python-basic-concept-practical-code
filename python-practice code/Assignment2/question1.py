# 1. Write a port scanner without using nmap python module
import socket

def scan_ports(host, start_port, end_port):
    print(f"Scanning {host} from port {start_port} to {end_port}...")
    open_ports = []
    for port in range(start_port, end_port + 1):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.5)
            try:
                result = s.connect_ex((host, port))
                if result == 0:
                    open_ports.append(port)
            except Exception:
                pass
    if open_ports:
        print(f"Open ports on {host}: {open_ports}")
    else:
        print(f"No open ports found on {host} in range {start_port}-{end_port}")

if __name__ == "__main__":
    target_host = input("Enter target host (IP or domain): ")
    start = int(input("Enter start port: "))
    end = int(input("Enter end port: "))
    scan_ports(target_host, start, end)