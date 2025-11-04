#!/bin/bash
# Django Ledger Health Check Script

# Check if Gunicorn is running
if pgrep -f gunicorn > /dev/null; then
    echo "✅ Gunicorn is running"
    
    # Check if server responds
    if curl -s -o /dev/null -w "%{http_code}" http://localhost:8000/ | grep -q "200\|302"; then
        echo "✅ Server is responding"
        echo "✅ Django Ledger is healthy"
        exit 0
    else
        echo "❌ Server is not responding"
        exit 1
    fi
else
    echo "❌ Gunicorn is not running"
    exit 1
fi
