# Log File Monitoring and Analysis

This repository contains scripts and instructions for monitoring and analyzing log files using shell scripts and Python scripts.
## Setup Instructions

Before running the scripts, ensure you have the following:

- Docker installed on your system
- Basic knowledge of using Docker containers
because i have created docker container and i excuted this scripts in it
## Usage

### Shell Script (log-observe.sh)

To monitor a log file in real-time using the shell script:

```bash
sh log-observe.sh
*Creativity and additional features implemented beyond basic requirements*
This script will continuously monitor the specified log file and highlight specific keywords such as "ERROR" and "404" with different colors for better visibility.
## Explanation

### Shell Script (log-observe.sh)

The `log-observe.sh` script uses the `tail` command to continuously monitor a specified log file (`/var/log/nginx/host.access.log` by default). It reads new log entries in real-time and applies colors to highlight specific keywords such as "ERROR" and "404" for better visibility.

The log_monitor.py script performs the following tasks:

Continuous Log Monitoring: The script continuously monitors the specified log file in real-time using the tail command.
Color-Coded Log Messages: Log messages are color-coded for better visibility. You can customize the colors and formatting as needed.
Customizable Keywords: The script allows you to specify a list of keywords to monitor and count occurrences. You can update the keywords list in the script to include specific keywords relevant to your log analysis.
Summary Report: The script generates a summary report of the log analysis, including the count of occurrences for each keyword.
Conclusion
The log_monitor.py script provides a convenient way to monitor log files and perform basic log analysis. It can be customized and extended to suit different use cases and requirements
