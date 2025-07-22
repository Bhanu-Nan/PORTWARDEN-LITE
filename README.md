🚨 PortWarden Lite
Because your ports deserve a bodyguard.

🔍 What is PortWarden Lite?
PortWarden Lite is a lightweight, zero-fluff network monitoring tool built to scan, track, and alert on open ports of a target system. Whether you’re a hacker, sysadmin, or a curious soul who just wants to watch their digital borders — this tool has your back.

Think of it like a watchdog for your ports:

🧠 Remembers what ports were open last time

👀 Notices when new ones open or old ones close

🔔 Sends alerts straight to your Discord like a loyal sidekick

🕒 Automates everything on schedule with cron

⚙️ Features
✅ Scan live open ports using nmap
✅ Detect changes in port states (added/removed)
✅ Historical logging with JSON
✅ Custom Discord alerts
✅ Easy to automate with cron
✅ Fully open-source, readable and modifiable

📂 Folder Structure
bash
Copy
Edit
PORTWARDEN_PROJECT/
├── cron.log                  # Auto-scan logs
├── run_portwarden.sh         # One-click launcher
├── src/
│   ├── scanner.py            # Scans and saves current open ports
│   ├── portwatcher.py        # Compares with previous scan, detects changes
│   ├── alert.py              # Sends Discord alerts
│   ├── ports.json            # Current scan
│   ├── prev_ports.json       # Previous scan
│   ├── port_history.json     # Log of all port changes
│   └── run_portwarden.sh     # (Optional duplicate runner)
🚀 How to Use
🔧 Step 1: Install Requirements
bash
Copy
Edit
sudo apt install nmap -y
pip install requests
📦 Step 2: Clone the Repo
bash
Copy
Edit
git clone https://github.com/YourUsername/PORTWARDEN-LITE.git
cd PORTWARDEN-LITE
🧪 Step 3: First Manual Run
bash
Copy
Edit
python3 src/scanner.py
python3 src/portwatcher.py <target_IP_or_hostname>
Example:

bash
Copy
Edit
python3 src/portwatcher.py scanme.nmap.org
This will generate the first ports.json and start logging changes.

🤖 Setting Up Cron (Optional but Powerful)
Automate scans every X minutes/hours.

Open the crontab editor:
bash
Copy
Edit
crontab -e
Add this line (runs every hour):
bash
Copy
Edit
0 * * * * /usr/bin/python3 /your/path/to/src/portwatcher.py scanme.nmap.org >> /your/path/to/cron.log 2>&1
Save and exit. Now your tool works silently, watching 👀.

💬 Discord Alert Setup (Optional)
To get real-time alerts:

Create a webhook in your Discord server.

Copy the webhook URL.

Replace YOUR_DISCORD_WEBHOOK_HERE in src/alert.py with your URL.

Done. Every port change pings you like a boss.

📸 Screenshots 
![Scanner Output](screenshots/scanner_output.png)
![Discord Alert](screenshots/discord_alert.png)


 Can I Modify This?
YES.
This project is open source, no gatekeeping here. Fork it, tweak it, break it, rebuild it, ship it.

You wanna turn this into a full-blown dashboard app?
You wanna make it send alerts to Telegram instead?
Go wild, just give credit if you remix it.

🙌 Built With:
🐍 Python 3

🛠️ Nmap

🪄 Cron

💬 Discord Webhooks

👤 Author
 Made by NANDHANA R S
A CS student with a passion for cybersecurity and building real stuff.

If this project helped you, give it a ⭐ star!
Or better yet, contribute! Pull requests are welcome.
