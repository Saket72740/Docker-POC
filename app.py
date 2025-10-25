from flask import Flask, jsonify, request
import psycopg2
import os
import psutil

import logging

app = Flask(__name__)

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

DB_HOST = os.getenv('DB_HOST', 'db') 
DB_NAME = os.getenv('POSTGRES_DB', 'testdb')
DB_USER = os.getenv('POSTGRES_USER', 'postgres')
DB_PASSWORD = os.getenv('POSTGRES_PASSWORD', 'password')

def get_db_connection():
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )
        cur = conn.cursor()
        cur.execute("SELECT version();")
        version = cur.fetchone()
        cur.close()
        conn.close()
        return version[0]
    except Exception as e:
        return str(e)

@app.route('/', methods=['GET'])
def home():
    if request.method == 'GET':
        version = get_db_connection()
        response = {
            "message": "Hello, I am running inside a Docker container! 🚀",
            "postgres_version": version,
            "status": "success",
            "method": "GET"
        }
        logger.info(f"Endpoint '/' called. Response: {response}")
        return jsonify(response), 200

@app.route('/metrics', methods=['GET'])
def get_metrics():
    stats = {
        "container_id": os.uname().nodename,
        "cpu_percent": psutil.cpu_percent(interval=1),
        "memory_percent": psutil.virtual_memory().percent,
        "disk_percent": psutil.disk_usage("/").percent,
        "network_io": psutil.net_io_counters()._asdict()
    }
    return stats, 200   

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)