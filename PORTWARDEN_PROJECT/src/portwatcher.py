#!/usr/bin/env python3

import socket
import requests
import json
import datetime
import argparse
import subprocess

# ========== CONFIGS ==========
DISCORD_WEBHOOK = "https://discord.com/api/webhooks/1396897949480521878/s1513hzf2iTWMBmMY1DUmwBo0XReSB96wdIC0lOaKI5Rd4JV>"
PORT_RANGE = range(1, 1025)

# ========== ALERTS ==========
def send_discord_alert(message):
    try:
        payload = {"content": message}
        requests.post(DISCORD_WEBHOOK, json=payload)
    except Exception as e:
        print(f" Discord alert failed: {e}")

# ========== GEOLOCATION ==========
def get_geolocation(ip):
    try:
        response = requests.get(f"https://ipinfo.io/{ip}/json")
        data = response.json()
        return {
            "ip": data.get("ip"),
            "country": data.get("country"),
            "region": data.get("region"),
            "city": data.get("city"),
            "org": data.get("org")
        }
    except Exception as e:
        return {"error": str(e)}

# ========== PORT SCAN ==========
def scan_ports(target):
    open_ports = []
    print(f"🛰 Scanning {target} from port 1 to 1024...\n")

    for port in PORT_RANGE:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.5)
            result = s.connect_ex((target, port))
            if result == 0:
                open_ports.append(port)
            s.close()
        except socket.gaierror:
            send_discord_alert(f"❌ Could not resolve hostname {target}")
            print("❌ Could not resolve hostname.")
            return []
        except socket.error:
            send_discord_alert(f"❌ Couldn't connect to server {target}")
            print("❌ Couldn't connect to server.")
            return []
    return open_ports

# ========== NMAP SCAN ==========
def run_nmap(target):
    try:
        result = subprocess.run(["nmap", "-sV", target], capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        send_discord_alert(f"❌ Nmap scan failed for {target}: {e}")
        return f"Nmap failed: {e}"

# ========== MAIN ==========
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="PortWardenLite: Lightweight Port Monitor")
    parser.add_argument("target", help="Target IP or hostname")
    parser.add_argument("--nmap", action="store_true", help="Run Nmap after basic scan")
    args = parser.parse_args()

    target = args.target
    try:
        ip = socket.gethostbyname(target)
        geo = get_geolocation(ip)

        print("\n Target Info:")
        print(f"  IP: {geo.get('ip')}")
        print(f"  Country: {geo.get('country')}")
        print(f"  Region: {geo.get('region')}")
        print(f"  City: {geo.get('city')}")
        print(f"  ISP: {geo.get('org')}\n")

        # Run port scan
        open_ports = scan_ports(target)
        if open_ports:
            print("\n Open Ports:")
            for port in open_ports:
                try:
                    service = socket.getservbyport(port)
                except:
                    service = "unknown"
                print(f"  [OPEN] Port {port} ({service})")
            alert_msg = f" PortWardenLite Alert: `{target}` has {len(open_ports)} open ports.\n" + \
                        "\n".join([f" Port {p}" for p in open_ports])
            send_discord_alert(alert_msg)
        else:
            print(" No open ports found.")
            send_discord_alert(f" PortWardenLite: No open ports found on `{target}`.")

        # Optional Nmap scan
        if args.nmap:
            print("\n Running Nmap...\n")
            nmap_result = run_nmap(target)
            print(nmap_result)
            if len(nmap_result) > 1900:
                nmap_result = nmap_result[:1900] + "...\n[truncated]"
            send_discord_alert(f"📡 Nmap scan for `{target}`:\n```{nmap_result}```")

        # Timestamp the scan
        now = datetime.datetime.now()
        print(f"\n Scan finished at: {now}")
        print(" Done.")

    except Exception as e:
        print(f" Unexpected error: {e}")
        send_discord_alert(f" PortWardenLite crashed scanning `{target}`:\n{e}")
