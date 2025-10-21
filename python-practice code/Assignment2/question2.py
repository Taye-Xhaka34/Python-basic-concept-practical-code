# simple_port_scanner.py
# 1) socket-based scanner (pure Python)
# 2) nmap-based scanner (uses python-nmap)

import socket
import sys

try:
    import nmap  # python-nmap
except ImportError:
    nmap = None  # we'll check later if user chooses option 2

def scan_ports_socket(target, start_port, end_port, timeout=0.5):
    """Scan ports using Python sockets (TCP connect)."""
    print(f"\n[socket] Scanning {target} from port {start_port} to {end_port}...")
    try:
        for port in range(start_port, end_port + 1):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(timeout)
            result = s.connect_ex((target, port))
            if result == 0:
                print(f"Port {port}: OPEN")
            s.close()
    except KeyboardInterrupt:
        print("\nScan cancelled by user.")
    except socket.gaierror:
        print("Hostname could not be resolved. Check the target name.")
    except Exception as e:
        print("Error:", e)

def nmap_scan(target, start_port, end_port):
    """Scan ports using python-nmap (wrapping nmap)."""
    if nmap is None:
        print("python-nmap library is not installed. Install with: pip install python-nmap")
        return

    nm = nmap.PortScanner()
    port_range = f"{start_port}-{end_port}"
    print(f"\n[nmap] Scanning {target} ports {port_range} with nmap...")
    try:
        nm.scan(hosts=target, ports=port_range, arguments='-sT')  # -sT uses TCP connect scan
    except nmap.PortScannerError as e:
        print("Nmap error:", e)
        return
    except Exception as e:
        print("Unexpected error:", e)
        return

    hosts = nm.all_hosts()
    if not hosts:
        print("No hosts found (maybe the name couldn't be resolved or host is down).")
        return

    for h in hosts:
        print(f"\nHost: {h} ({nm[h].hostname()})")
        for proto in nm[h].all_protocols():
            lports = sorted(nm[h][proto].keys())
            for port in lports:
                state = nm[h][proto][port]['state']
                name = nm[h][proto][port].get('name', '')
                print(f"Port {port}\tState: {state}\tService: {name}")

def get_int(prompt, default=None):
    """Helper to safely get integer input."""
    while True:
        val = input(prompt).strip()
        if val == "" and default is not None:
            return default
        try:
            return int(val)
        except ValueError:
            print("Please enter a valid integer.")

def main():
    print("Choose scanner:\n 1) socket (simple)\n 2) nmap (requires python-nmap)")
    choice = input("Choose scanner [1/2]: ").strip()

    target = input("Enter target host (IP or domain): ").strip()
    if not target:
        print("No target provided. Exiting.")
        sys.exit(1)

    start = get_int("Enter start port (e.g. 1): ", default=1)
    end = get_int("Enter end port (e.g. 1024): ", default=1024)
    if start < 1 or end > 65535 or start > end:
        print("Invalid port range. Ports must be 1-65535 and start <= end.")
        sys.exit(1)

    if choice == "1":
        scan_ports_socket(target, start, end)
    elif choice == "2":
        nmap_scan(target, start, end)
    else:
        print("Invalid choice. Exiting.")

if __name__ == "__main__":
    main()
