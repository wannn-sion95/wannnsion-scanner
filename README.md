markdown
# WannnSion Scanner

A simple and fast port scanner built with Python. Uses multithreading to scan ports quickly, detects common services, and grabs banners from open ports.

| | / /___ _____ ____ / /()_ ____
| | /| / / __ `/ __ / __ \ __ / / __ / __
| |/ |/ / // / / / / / / / / / / // / / / /
|/|__/_,// /// // ///_// /_/


## Features

- Fast multithreaded scanning
- Automatic service detection (HTTP, PostgreSQL, etc.)
- Banner grabbing from open ports
- No external dependencies, pure Python

## Requirements

- Python 3.8 or higher

## Installation

git clone https://github.com/wannn-sion95/wannnsion-scanner.git
cd wannnsion-scanner


## Usage

python3 wannnsion_scanner.py <target> -p <port_range> -t <threads>


Examples:

python3 wannnsion_scanner.py 127.0.0.1 -p 1-1000
python3 wannnsion_scanner.py 127.0.0.1 -p 1-65535 -t 200
python3 wannnsion_scanner.py -V


Options:

- `target` — IP address or hostname to scan
- `-p`, `--ports` — Port range to scan, format `start-end` (default: 1-1024)
- `-t`, `--threads` — Number of threads to use (default: 100)
- `-V`, `--version` — Show version info

## Example Output

[OPEN] Port 80 http HTTP/1.1 200 OK
[OPEN] Port 5432 postgresql


## Disclaimer

This tool is intended for educational purposes and authorized security testing only. Only use it on systems and networks you own or have explicit permission to test. Unauthorized scanning of systems you do not own may be illegal in your jurisdiction.

## Roadmap

- Save scan results to a file
- Progress indicator during scans
- Basic OS detection

## Author

Wannn Sion — [@wannn-sion95](https://github.com/wannn-sion95)

## License

MIT License
