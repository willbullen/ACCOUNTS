#!/bin/bash

# Django Ledger Auto-Restart Monitor
# This script checks if Gunicorn is running and restarts it if needed

PROJECT_DIR="/home/ubuntu/django-accounting-system"
LOG_FILE="/home/ubuntu/monitor.log"
PID_FILE="/home/ubuntu/gunicorn.pid"

# Function to check if Gunicorn is running
is_running() {
    if pgrep -f "gunicorn dev_env.wsgi" > /dev/null; then
        return 0
    else
        return 1
    fi
}

# Function to start Gunicorn
start_gunicorn() {
    echo "[$(date)] Starting Gunicorn..." >> "$LOG_FILE"
    cd "$PROJECT_DIR"
    gunicorn dev_env.wsgi:application \
        --bind 0.0.0.0:8000 \
        --workers 2 \
        --daemon \
        --pid "$PID_FILE" \
        --access-logfile /home/ubuntu/gunicorn-access.log \
        --error-logfile /home/ubuntu/gunicorn-error.log \
        --timeout 120 \
        --max-requests 1000 \
        --max-requests-jitter 50
    
    if [ $? -eq 0 ]; then
        echo "[$(date)] Gunicorn started successfully" >> "$LOG_FILE"
    else
        echo "[$(date)] ERROR: Failed to start Gunicorn" >> "$LOG_FILE"
    fi
}

# Main monitoring logic
if ! is_running; then
    echo "[$(date)] Gunicorn is not running. Attempting to restart..." >> "$LOG_FILE"
    start_gunicorn
else
    # Check if server is responding
    if ! curl -s -o /dev/null -w "%{http_code}" http://localhost:8000/ | grep -q "200\|302"; then
        echo "[$(date)] Server not responding. Restarting Gunicorn..." >> "$LOG_FILE"
        pkill -f "gunicorn dev_env.wsgi"
        sleep 2
        start_gunicorn
    fi
fi
