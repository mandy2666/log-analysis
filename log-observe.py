#!/usr/bin/env python3
import time
import os

# Define the log file to monitor
LOG_FILE = "/var/log/nginx/host.access.log"

# Define keywords to monitor and their corresponding colors
KEYWORDS = {
    "ERROR": "\033[91m",  # Red color for ERROR
    "404": "\033[93m",     # Yellow color for 404
    # Add more keywords and colors as needed
}

def analyze_log(log_file):
    # Open the log file in read mode
    with open(log_file, 'r') as file:
        # Read all lines from the log file
        lines = file.readlines()

        # Initialize keyword counts
        keyword_counts = {keyword: 0 for keyword in KEYWORDS}

        # Count occurrences of specific keywords or patterns
        for line in lines:
            for keyword in KEYWORDS:
                if keyword in line:
                    keyword_counts[keyword] += 1
                    print(KEYWORDS[keyword] + line.strip() + "\033[0m")  # Print with color

        # Generate summary report
        report = "Summary Report:\n"
        for keyword, count in keyword_counts.items():
            report += f"{keyword}: {count}\n"

        # Save the summary report to a file
        with open("log_summary.txt", "w") as report_file:
            report_file.write(report)

if __name__ == "__main__":
    print("Monitoring and analyzing log file:", LOG_FILE)
    try:
        while True:
            # Perform log analysis
            analyze_log(LOG_FILE)

            # Sleep for a short interval
            time.sleep(5)  # Adjust the interval as needed
    except KeyboardInterrupt:
        print("\nMonitoring interrupted. Exiting.")
