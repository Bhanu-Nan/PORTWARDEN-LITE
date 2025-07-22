import socket
import time

def scan_ports(target_ip, port_range=(1, 1024), timeout=0.5):
    print(f"Scanning {target_ip} from port {port_range[0]} to {port_range[1]}...\n")
    open_ports = []

    for port in range(port_range[0], port_range[1] + 1):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(timeout)
            result = s.connect_ex((target_ip, port))
            if result == 0:
                try:
                    service = socket.getservbyport(port)
                except:
                    service = "Unknown"
                print(f"[OPEN] Port {port} ({service})")
                open_ports.append(port)
    
    print(f"\n Scan complete. {len(open_ports)} open ports found.")
    return open_ports

if __name__ == "__main__":
    target = input("Enter target IP or hostname: ").strip()
    start = time.time()
    scan_ports(target, port_range=(1, 1024))
    print(f"Duration: {round(time.time() - start, 2)} seconds")
