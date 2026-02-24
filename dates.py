from datetime import datetime, timedelta
import time


now = datetime.now()


yesterday = now - timedelta(days=1)


tomorrow = now + timedelta(days=1)

next_week = now + timedelta(days=7)


date1 = datetime(2025, 1, 1)
date2 = datetime(2025, 12, 31)
difference = date2 - date1


formatted = now.strftime("%Y-%m-%d %H:%M:%S")


parsed = datetime.strptime("2025-02-20", "%Y-%m-%d")


timestamp = now.timestamp()


from_timestamp = datetime.fromtimestamp(timestamp)