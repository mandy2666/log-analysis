#!/bin/bash

# Define the log file to monitor
LOG_FILE="/var/log/nginx/host.access.log"

# Function to handle cleanup
cleanup() {
    echo "Stopping log monitoring..."
    exit 0
}

# Trap Ctrl+C and call cleanup function
trap cleanup INT

echo "Monitoring log file: $LOG_FILE"
echo "Press Ctrl+C to stop monitoring..."

# Monitor log file continuously
tail -n0 -f "$LOG_FILE" | while read line; do
    # Check for keywords and apply colors
    if [[ $line == *"ERROR"* ]]; then
        echo -e "\033[91m$line\033[0m"  # Red color for ERROR
    elif [[ $line == *"404"* ]]; then
        echo -e "\033[93m$line\033[0m"  # Yellow color for 404
    else
        echo "$line"  # No color for other lines
    fi
done
