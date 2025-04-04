# 📘 Real-Time Log Generator in Python

This project simulates **real-time server log generation** using Python.  
It's ideal for testing log monitoring systems, dashboards, or simulating backend activity.

---

## 🌟 Features

- 🕒 Generates logs every 2 seconds  
- 🔁 Randomized log messages for realism  
- 🚦 Log levels: `INFO`, `WARNING`, `ERROR`, `CRITERIA`  
- 📝 Writes to a `.log` file with timestamp  
- 📤 Console output for real-time tracking  
- ✅ Easy to stop with `Ctrl + C`

---

## 🧠 Python Code: `log_generator.py`

```python
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  3 15:16:26 2025
@author: sakuc
"""

import time
import random

LOG_FILE = "C:/1-python/server.log"
LOG_LEVELS = ["INFO", "WARNING", "ERROR", "CRITERIA"]

MESSAGES = [
    "User is logged in : user123",
    "High memory usage detected",
    "Database connection failed : timeout",
    "File uploaded : report.pdf",
    "Server crash detected! Restarting",
    "User logged out : user456"
]

def generator_logs():
    # Continuously writes logs in file every 2 seconds
    with open(LOG_FILE, "a") as file:
        while True:
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
            log_level = random.choice(LOG_LEVELS)
            message = random.choice(MESSAGES)
            log_entry = f"{timestamp} {log_level} {message}\n"
            file.write(log_entry)
            file.flush()  # Ensure immediate writing
            print(f"Generated log: {log_entry.strip()}")
            time.sleep(2)  # Simulate real-time logging

generator_logs()
