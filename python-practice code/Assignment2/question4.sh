# 4. Write a tool in bash that accepts IP, and NSE script name then it will run nmap scan
#!/bin/bashs
# Usage: ./nmap_nse_scan.sh <IP> <NSE_script>
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <IP> <NSE_script>"
    exit 1
fi

IP="$1"
NSE_SCRIPT="$2"

echo "Running nmap scan on $IP with NSE script $NSE_SCRIPT..."
nmap --script "$NSE_SCRIPT" "$IP"

