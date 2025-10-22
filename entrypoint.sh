python sys_monitor.py  > /proc/1/fd/1 2>&1 &
exec python -m flask run --host=0.0.0.0 --port=5000