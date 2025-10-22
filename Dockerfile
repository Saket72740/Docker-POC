FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    gcc \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .
COPY sys_monitor.py .
COPY entrypoint.sh .

RUN sed -i 's/\r$//' entrypoint.sh && \
    chmod +x entrypoint.sh

EXPOSE 5000

# CMD ["python", "app.py"]
# CMD ["python", "sys_monitor.py"]
CMD ["./entrypoint.sh"]