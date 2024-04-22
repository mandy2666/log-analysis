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

## The log_monitor.py script performs the following tasks:

Continuous Log Monitoring: The script continuously monitors the specified log file in real-time using the tail command.
Color-Coded Log Messages: Log messages are color-coded for better visibility. You can customize the colors and formatting as needed.
Customizable Keywords: The script allows you to specify a list of keywords to monitor and count occurrences. You can update the keywords list in the script to include specific keywords relevant to your log analysis.
Summary Report: The script generates a summary report of the log analysis, including the count of occurrences for each keyword.
Conclusion
The log_observe.py script provides a convenient way to monitor log files and perform basic log analysis. It can be customized and extended to suit different use cases and requirements
extra added in scripts
$Color-coded log messages for better visibility.
$Configurable list of keywords to monitor and count.
$Option to save the summary report to a file.

outcome in log_observe.py

Monitoring and analyzing log file: /var/log/nginx/host.access.log
172.17.0.1 - - [22/Apr/2024:16:16:07 +0000] "GET /earth.jpg HTTP/1.1" 404 555 "http://127.0.0.1/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0" "-"
172.17.0.1 - - [22/Apr/2024:16:16:07 +0000] "GET /earth.jpg HTTP/1.1" 404 555 "http://127.0.0.1/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0" "-"
172.17.0.1 - - [22/Apr/2024:16:16:07 +0000] "GET /earth.jpg HTTP/1.1" 404 555 "http://127.0.0.1/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0" "-"
172.17.0.1 - - [22/Apr/2024:16:16:07 +0000] "GET /earth.jpg HTTP/1.1" 404 555 "http://127.0.0.1/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0" "-"
172.17.0.1 - - [22/Apr/2024:16:16:07 +0000] "GET /earth.jpg HTTP/1.1" 404 555 "http://127.0.0.1/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0" "-"

outcome in log_observe.sh

root@88336b3891b9:/usr/local/bin# sh log-observe.sh
Monitoring log file: /var/log/nginx/host.access.log
Press Ctrl+C to stop monitoring...
log-observe.sh: 21: [[: not found
log-observe.sh: 23: [[: not found
172.17.0.1 - - [22/Apr/2024:16:55:07 +0000] "GET / HTTP/1.1" 304 0 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0" "-"
log-observe.sh: 21: [[: not found
log-observe.sh: 23: [[: not found
172.17.0.1 - - [22/Apr/2024:16:55:07 +0000] "GET /earth.jpg HTTP/1.1" 404 555 "http://127.0.0.1/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0" "-"

and extra files added in github
  Dockerfile for dockerize the web application and analysis the logs
  index.html for web application
 docker build -t my-nginx-container . #use this command for build the dockerfile
 docker run -itd -p 80:80 -t my-nginx-container #use this command for run the docker container and open port:80








