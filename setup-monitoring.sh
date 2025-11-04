#!/bin/bash

# Setup monitoring cron job for Django Ledger
# This will check every 5 minutes if the server is running

MONITOR_SCRIPT="/home/ubuntu/django-accounting-system/monitor-and-restart.sh"

# Check if cron job already exists
if crontab -l 2>/dev/null | grep -q "$MONITOR_SCRIPT"; then
    echo "Monitoring cron job already exists"
else
    # Add cron job to check every 5 minutes
    (crontab -l 2>/dev/null; echo "*/5 * * * * $MONITOR_SCRIPT") | crontab -
    echo "Monitoring cron job added successfully"
    echo "The server will be automatically checked and restarted if needed every 5 minutes"
fi

# Display current crontab
echo ""
echo "Current cron jobs:"
crontab -l
