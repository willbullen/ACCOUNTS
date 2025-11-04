#!/bin/bash

# Django Ledger Production Startup Script (Improved)
# This script ensures the server starts reliably with proper configuration

set -e  # Exit on error

PROJECT_DIR="/home/ubuntu/django-accounting-system"
PID_FILE="/home/ubuntu/gunicorn.pid"

echo "=== Django Ledger Production Startup ==="
echo "Starting at: $(date)"

# Navigate to project directory
cd "$PROJECT_DIR"

# Kill any existing Gunicorn processes
echo "Stopping any existing Gunicorn processes..."
pkill -f "gunicorn dev_env.wsgi" || true
sleep 2

# Remove old PID file if exists
rm -f "$PID_FILE"

# Start Gunicorn with production settings
echo "Starting Gunicorn..."
gunicorn dev_env.wsgi:application \
    --bind 0.0.0.0:8000 \
    --workers 2 \
    --daemon \
    --pid "$PID_FILE" \
    --access-logfile /home/ubuntu/gunicorn-access.log \
    --error-logfile /home/ubuntu/gunicorn-error.log \
    --log-level info \
    --timeout 120 \
    --max-requests 1000 \
    --max-requests-jitter 50 \
    --worker-class sync

# Wait a moment for startup
sleep 3

# Verify it's running
if pgrep -f "gunicorn dev_env.wsgi" > /dev/null; then
    echo "✅ Gunicorn started successfully"
    echo "   PID: $(cat $PID_FILE 2>/dev/null || echo 'N/A')"
    echo "   Workers: $(pgrep -f "gunicorn dev_env.wsgi" | wc -l)"
    echo "   URL: https://8000-i3y1v9m0ix2tfelzp3o48-394a41a8.manusvm.computer/"
    
    # Test if server is responding
    sleep 2
    if curl -s -o /dev/null -w "%{http_code}" http://localhost:8000/ | grep -q "200\|302"; then
        echo "✅ Server is responding to requests"
    else
        echo "⚠️  Server started but not responding yet (may need more time)"
    fi
else
    echo "❌ Failed to start Gunicorn"
    echo "Check logs at:"
    echo "  - /home/ubuntu/gunicorn-error.log"
    echo "  - /home/ubuntu/gunicorn-access.log"
    exit 1
fi

echo "=== Startup Complete ==="
