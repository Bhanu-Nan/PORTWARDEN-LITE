PortWardenLite – Lightweight Port Change Monitor

PortWardenLite is a personal project I built to scratch an itch — I wanted a dead-simple, no-BS tool that could watch open ports on any target and tell me when something changed. That's it. No heavy frameworks. No dashboards. Just Python, automation, and alerts that actually matter.

⚡ What it does

Scans a target machine or domain at regular intervals

Compares the current open ports to the previous state

Logs any differences — newly opened or closed ports

Sends an alert to Discord (or just logs it quietly if you prefer)


Think of it like motion detection — but for ports.

Why I Built It

I was learning about network security and realized how many services can quietly pop up or shut down on machines, especially in dynamic environments.
A small change can mean:

A new service spun up (legit or malicious)

An accidental exposure

Or worse, someone probing from inside


So I built PortWardenLite — a minimal tool that just does the job.

How it works

1. You give it a target (like scanme.nmap.org)


2. It runs an nmap scan in the background


3. It saves the result as JSON


4. Compares with the last scan


5. Logs any changes


6. (Optional) Sends alerts to Discord



It’s automated using cron on Linux, so it can run every hour, every day — whatever you need.


Getting Started (Linux/Kali)

# Clone the repo
git clone https://github.com/Bhanu-Nan/PORTWARDEN-LITE.git
cd PORTWARDEN-LITE

# Install dependencies
sudo apt update
sudo apt install nmap python3-pip
pip3 install -r requirements.txt

# Add your Discord webhook
nano .env

Example .env:

DISCORD_WEBHOOK=https://discord.com/api/webhooks/your-webhook


---

🔁 Automate with Cron

Run this to edit your crontab:

crontab -e

Add this line to run every hour:

0 * * * * /usr/bin/python3 /path/to/portwatcher.py scanme.nmap.org >> /path/to/cron.log 2>&1

Replace /path/to/ with the full path to your script.

## 📸 Sample Screenshots
https://github.com/Bhanu-Nan/PORTWARDEN-LITE/tree/main/PORTWARDEN_PROJECT/src/docs/PortWarden.docs


🙋‍♂️ Author
Nandhana R S 
Made with frustration and fascination 
I’m a CS undergrad with a minor in cyber, just building things that solve real problems.

