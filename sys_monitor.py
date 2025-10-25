import psutil
import time
import os

def show_system_stats():
    print("System Monitoring Tool")
    print("======================")

    while True:
        memory = psutil.virtual_memory()
        process_count = len(psutil.pids())
        uptime_seconds = time.time() - psutil.boot_time()

        print(f"CPU Usage: {psutil.cpu_percent(interval=1)}%")
        print(f"Memory Usage: {memory.percent}% of {round(memory.total / (1024**3), 2)} GB")
        print(f"Disk Usage: {psutil.disk_usage('/').percent}%")
        print(f"Network Sent: {psutil.net_io_counters().bytes_sent / (1024 * 1024):.2f} MB")
        print(f"Network Received: {psutil.net_io_counters().bytes_recv / (1024 * 1024):.2f} MB")
        print(f"Total Processes: {process_count}")
        print(f"System Uptime: {round(uptime_seconds / 3600, 2)} hours")
        print("======================") 


if __name__ == "__main__":
    print(f"Running as user: {os.getenv('USER', 'unknown')}")
    show_system_stats()