# Personal Web Server with System Monitoring

A containerized Flask web server with system monitoring and PostgreSQL database integration.

## Project Structure
```
personal_web_server/
├── app.py              # Main Flask application
├── sys_monitor.py      # System monitoring script
├── Dockerfile          # Docker container configuration
├── docker-compose.yml  # Multi-container Docker configuration
├── entrypoint.sh      # Container startup script
├── requirements.txt    # Python dependencies
└── logs/              # Application logs directory
```

## Features
- Flask web server with REST API endpoints
- Real-time system monitoring and logging
- PostgreSQL database integration
- Docker containerization
- Volume persistence for logs and data
- Network isolation using Docker networks

## Prerequisites
- Docker
- Docker Compose
- Python 3.11+

## Environment Variables
```
Ask developer to share .env file
```

## API Endpoints
- `GET /` - Health check endpoint
- `GET /metrics` - System metrics
- `POST /save` - Save data to persistent storage
- `GET /read` - Read saved data
- `GET /logs` - View system logs

## Installation & Setup
1. Clone the repository:
```bash
git clone <repository-url>
cd personal_web_server
```

2. Build and start the containers:
```bash
docker-compose up --build
```

3. Access the application:
```bash
curl http://localhost:8080
```

## Development
- Logs are stored in `./logs` directory
- Application data persists in Docker volumes
- Database data persists in `db_data` volume
- Source code changes reflect upon container restart

## Docker Commands
```bash
# Start containers in background
docker-compose up -d

# View logs
docker-compose logs -f

# Stop containers
docker-compose down

# Access PostgreSQL
docker-compose exec db psql -U postgres -d testdb
```

## Contributing

```
If you want to contribute anything: 

1. Fork the repository
2. Create your feature branch
3. Submit a pull request
```
