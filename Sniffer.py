"""
Simple Packet Sniffer
- Requires: scapy
- Run as root/administrator (e.g., sudo python3 sniffer.py)
"""

from scapy.all import sniff, PcapWriter
from datetime import datetime

# --- Configuration ---
INTERFACE = None         # e.g., "eth0" or "wlan0" or None for default
COUNT = 0                # number of packets to capture (0 means forever)
BPF_FILTER = ""          # BPF filter string, e.g. "tcp port 80" or "" for all
SAVE_PCAP = "capture.pcap"   # set to None to skip saving to file

# --- Helper to format packet info simply ---
def format_packet(pkt):
    """
    Build a short readable summary for the given packet.
    We try to show timestamp, src, dst, protocol and length.
    """
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    src = pkt.src if hasattr(pkt, "src") else "-"
    dst = pkt.dst if hasattr(pkt, "dst") else "-"
    proto = pkt.sprintf("%IP.proto%") if pkt.haslayer("IP") else pkt.name
    length = len(pkt)
    # Return one-line summary
    return f"{ts} | {src} -> {dst} | proto: {proto} | len: {length}"

# --- Packet callback function ---
def handle_packet(pkt):
    """
    This function is called for each captured packet.
    It prints a short summary and (optionally) writes the packet to a pcap file.
    """
    try:
        print(format_packet(pkt))
    except Exception:
        # Fallback to Scapy's summary if something unexpected happens
        print(pkt.summary())

    # If saving to pcap, scappy_writer is set globally
    if SAVE_PCAP:
        scappy_writer.write(pkt)

# --- Main sniff function ---
def start_sniff(interface=INTERFACE, count=COUNT, bpf_filter=BPF_FILTER, save_pcap=SAVE_PCAP):
    global scappy_writer
    scappy_writer = None

    if save_pcap:
        # PcapWriter appends packets to a file (creates file if missing)
        scappy_writer = PcapWriter(save_pcap, append=True, sync=True)
        print(f"[+] Saving captured packets to: {save_pcap}")

    print(f"[+] Starting packet capture on interface={interface!s} count={count} filter='{bpf_filter}'")
    try:
        # sniff blocks until count packets captured (if count>0), or until Ctrl+C
        sniff(iface=interface, prn=handle_packet, filter=bpf_filter, store=False, count=count)
    except PermissionError:
        print("✖ Permission denied: run the script with root/administrator privileges (e.g., sudo).")
    except KeyboardInterrupt:
        print("\n[!] Capture stopped by user (Ctrl+C).")
    finally:
        if scappy_writer:
            scappy_writer.close()
            print("[+] Pcap file closed.")

# --- Run when executed directly ---
if __name__ == "__main__":
    # Example usage:
    # - To sniff all traffic on default interface and save to capture.pcap:
    #     sudo python3 sniffer.py
    # - To sniff only HTTP traffic (port 80):
    #     set BPF_FILTER = "tcp port 80"
    # - To capture only 50 packets:
    #     set COUNT = 50
    # (You can change INTERFACE, COUNT, BPF_FILTER, SAVE_PCAP above or modify here.)
    start_sniff()
