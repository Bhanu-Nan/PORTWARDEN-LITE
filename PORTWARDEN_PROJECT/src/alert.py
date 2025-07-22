import requests 

# Paste your Discord webhook here 👇
DISCORD_WEBHOOK_URL="https://discord.com/api/webhooks/1396897949480521878/s1513hzf2iTWMBmMY1DUmwBo0XReSB96wdIC0lOaKI5Rd4JVp-KYKnuxQBUABOEEPiCU"

def send_alert(opened_ports, closed_ports, target):
    if not DISCORD_WEBHOOK_URL.startswith("https://discord.com/api/webhooks/"):
        print("🚫 Invalid webhook. Alert skipped.")
        return

    message = f"🔔 **PortWarden Alert for {target}** 🔔\n"

    if opened_ports:
        message += "\n🟢 **New Ports Opened:**\n"
        for port in opened_ports:
            message += f"➕ Port `{port}`\n"

    if closed_ports:
        message += "\n🔴 **Ports Closed:**\n"
        for port in closed_ports:
            message += f"➖ Port `{port}`\n"

    data = {"content": message}

    try:
        response = requests.post(DISCORD_WEBHOOK_URL, json=data)
        if response.status_code == 204:
            print("✅ Discord alert sent.")
        else:
            print(f"⚠️ Failed to send Discord alert: {response.status_code}")
    except Exception as e:
        print(f"❌ Error sending alert: {e}")
