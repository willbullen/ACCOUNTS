#!/bin/bash

# Django Ledger Dark Theme - Production Start Script

echo "Starting Django Ledger with Dark Theme..."

# Navigate to project directory
cd /home/ubuntu/django-accounting-system

# Stop any existing Gunicorn processes
echo "Stopping existing Gunicorn processes..."
pkill -f gunicorn
sleep 2

# Start Gunicorn
echo "Starting Gunicorn server..."
gunicorn dev_env.wsgi:application \
    --bind 0.0.0.0:8000 \
    --workers 2 \
    --timeout 120 \
    --daemon \
    --access-logfile /home/ubuntu/gunicorn-access.log \
    --error-logfile /home/ubuntu/gunicorn-error.log

# Check if started successfully
sleep 2
if ps aux | grep -v grep | grep gunicorn > /dev/null; then
    echo "✅ Django Ledger is now running!"
    echo "📍 URL: https://8000-i3y1v9m0ix2tfelzp3o48-394a41a8.manusvm.computer/"
    echo "👤 Login: admin / admin123"
    echo ""
    echo "📊 View logs:"
    echo "  Access: tail -f /home/ubuntu/gunicorn-access.log"
    echo "  Error:  tail -f /home/ubuntu/gunicorn-error.log"
else
    echo "❌ Failed to start Gunicorn. Check error log:"
    echo "  tail -f /home/ubuntu/gunicorn-error.log"
    exit 1
fi
