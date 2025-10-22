# Personal Web Server with System Monitoring

A containerized Flask web server with system monitoring capabilities built using Docker.

## Features

- Flask web server running on port 5000
- Real-time system monitoring including:
  - CPU usage
  - Memory usage
  - Disk usage
  - Network statistics
  - Process count
  - System uptime

## Prerequisites

- Docker
- Docker Compose

## Installation

1. Clone the repository:
```bash
git clone <your-repository-url>
cd personal_web_server
```

2. Build and run the container:
```bash
docker-compose up --build
```

## Usage

- Access the web server at: `http://localhost:8080`
- System monitoring stats are printed to the container logs

## Project Structure

```
personal_web_server/
├── app.py              # Flask web application
├── sys_monitor.py      # System monitoring script
├── Dockerfile         # Docker configuration
├── docker-compose.yml # Docker Compose configuration
└── requirements.txt   # Python dependencies
```
