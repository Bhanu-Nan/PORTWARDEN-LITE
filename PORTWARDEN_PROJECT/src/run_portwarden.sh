#!/bin/bash
echo "--- PortWardenLite Scan at $(date) ---" >> /home/bhanu/Desktop/PortWardenLite/cron.log
/home/bhanu/Desktop/PortWardenLite/venv/bin/python3 /home/bhanu/Desktop/PortWardenLite/src/portwatcher.py scanme.nmap.org >> /home/bhanu/Desktop/PortWardenLite/cron.log 2>&1
