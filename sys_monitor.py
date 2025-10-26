import datetime
import psutil
import time
import os
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

LOG_FILE = "/logs/access.log"

def show_system_stats():
    logger.info("System Monitoring Tool")
    logger.info("======================")

    while True:
        analyze_logs()
        memory = psutil.virtual_memory()
        process_count = len(psutil.pids())
        uptime_seconds = time.time() - psutil.boot_time()

        logger.info(f"CPU Usage: {psutil.cpu_percent(interval=1)}%")
        logger.info(f"Memory Usage: {memory.percent}% of {round(memory.total / (1024**3), 2)} GB")
        logger.info(f"Disk Usage: {psutil.disk_usage('/').percent}%")
        logger.info(f"Network Sent: {psutil.net_io_counters().bytes_sent / (1024 * 1024):.2f} MB")
        logger.info(f"Network Received: {psutil.net_io_counters().bytes_recv / (1024 * 1024):.2f} MB")
        logger.info(f"Total Processes: {process_count}")
        logger.info(f"System Uptime: {round(uptime_seconds / 3600, 2)} hours")
        logger.info("======================") 

def analyze_logs():
    logger.info("Starting log analysis...")
    try:
        if not os.path.exists(LOG_FILE):
            logger.info("No log file found. Waiting for logs...")
            return
        with open(LOG_FILE, "r") as f:
            lines = f.readlines()
        logger.info(f"Total log entries: {len(lines)}")

        error_count = sum(1 for line in lines if "ERROR" in line)
        warning_count = sum(1 for line in lines if "WARNING" in line)

        analysis_result = f"""
            Log Analysis Results ({datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')})
            ----------------------------------------
            Total log entries: {len(lines)}
            Errors: {error_count}
            Warnings: {warning_count}
            """
            
        logger.info(analysis_result)
            
        # Write analysis to a separate file
        analysis_file = os.path.join(LOG_DIR, "analysis.log")
        with open(analysis_file, "a") as f:
            f.write(analysis_result + "\n")
                
    except Exception as e:
        logger.info("Error analyzing logs: %s", str(e))


if __name__ == "__main__":
    logger.info(f"Running as user: {os.getenv('USER', 'unknown')}")

    show_system_stats()