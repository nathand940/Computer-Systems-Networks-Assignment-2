Student Name: Nathan Dolan
Student Number: 20059337
Project Name: Smart Study Buddy – Release 4


An IoT Monitoring System with Cloud Integration, Diagnostics, and Advanced Telemetry

## Overview
Smart Study Buddy (Release 4) is an enhanced IoT monitoring and diagnostics system built on a Raspberry Pi.
It integrates:
• 	Sense HAT temperature sensing
• 	Raspberry Pi Camera Module
• 	Secure MQTT communication
• 	Cloud dashboard (Adafruit IO)
• 	Local + cloud logging
• 	Automated file cleanup
• 	A full Health Check diagnostic system
Release 4 focuses on robustness, cloud integration, advanced telemetry, and self‑acquired features beyond the module requirements.

## Key Features (Release 4)

## Cloud Logging:

All major system events are published to a dedicated MQTT logs feed:

• System start/shutdown
• Temperature readings
• Image captures
• Monitoring cycles
• Cleanup actions
• Health Check results

This provides real‑time visibility into system behaviour.

## Health Check Diagnostic System (New in Release 4)

A new menu option performs a full system diagnostic:

• Camera test – verifies image capture
• Temperature sensor test – confirms Sense HAT is responding
• MQTT test – publishes a test message
• Disk space check – ensures sufficient free storage
• Cloud log output – results published to the logs feed
• Sense HAT feedback – visual confirmation

This demonstrates robustness, fault detection, and self‑learned system design.

## Monitoring Mode

Runs 5 automated cycles:

1. Capture image
2. Read temperature
3. Publish monitoring events
4. Log locally + cloud
5. Delay between cycles

All cycles are recorded in both local logs and cloud logs.

## Cloud Dashboard (Adafruit IO)

The dashboard includes:

• Temperature Line Chart
• Monitoring Stream
• Event Stream
• System Status Indicator
• System Logs Stream
• Optional: Image preview feed

This provides a clean, professional UI for remote monitoring.

## Local Logging System

Daily log files stored in:

  logs/studybuddy_YYYY-MM-DD.log

Includes:

• Info, warnings, errors
• Monitoring cycles
• Sensor readings
• Cleanup actions
• Health Check results

## Automated Cleanup

Old files are removed automatically:

• 	Images older than 7 days
• 	Logs older than 14 days

Cleanup events are logged locally and in the cloud.

## Modular Architecture

The system is split into clean, maintainable modules:

• main.py – menu system + orchestration
• camera_module.py – image capture
• temperature_module.py – Sense HAT temperature
• mqtt_module.py – secure MQTT communication
• sensehat_module.py – LED display functions
• cleanup_module.py – automated file cleanup
• logging_module.py – local logging setup
• config.py – credentials + feed names

This structure supports scalability, clarity, and professional design.

## System Architecture

Data Flow:

Sensors → Raspberry Pi → MQTT → Adafruit IO → Dashboard

## Dashboard Layout

The Adafruit IO dashboard includes:

• Temperature Line Chart
• Monitoring Stream Block
• Event Stream Block
• System Logs Stream Block
• Status Indicator (green = online, red = offline)
• Optional: Image feed preview

This provides a complete remote view of system activity.

## Health Check (Release 4 Feature)

The Health Check performs:

• Camera test
• Temperature sensor test
• MQTT test
• Disk space check
• Cloud log publishing
• Sense HAT visual feedback

Example output:

=== Running System Health Check ===
Camera: OK
Temperature Sensor: OK (28.7C)
MQTT: OK
Disk Space: 5123.4 MB free

Cloud logs show:

HealthCheck: Camera OK
HealthCheck: Temperature OK
HealthCheck: MQTT Test Message
HealthCheck: Disk 5123.4MB free

## Cleanup System

Automatically removes:

• Old images
• Old logs

This prevents storage issues and keeps the system running smoothly.

## Gitignore

A .gitignore file is used to keep the repository clean by preventing unnecessary or sensitive files from being uploaded to GitHub. For this project, it excludes:

• venv/ (virtual environment)
• __pycache__/ and *.pyc (Python cache files)
• logs/ (runtime logs)
• images/ (captured monitoring images)

This ensures that only the actual source code for Release 4 is tracked, keeping the repo secure, lightweight, and easy to review.


## Self‑Learned Technologies (Release 4 Requirement)

This project includes several features beyond module basics:

• Cloud logging architecture
• Multi‑feed MQTT design
• Diagnostic health check system
• Cloud dashboard design
• Modular Python architecture
• Automated cleanup routines
• Robust error handling
• Cloud‑based status monitoring

These demonstrate independent learning and advanced system design.

## Reflection & Future Improvements

What worked well:

• Modular design made debugging easy
• Cloud logging improved visibility
• Health Check added robustness
• Dashboard provided clear remote monitoring

Limitations:

• Dependent on Wi‑Fi
• Camera may fail in low light
• Adafruit IO rate limits

Future Enhancements:

• Configurable thresholds via dashboard
• Email/SMS alerts
• Long‑term data storage (Azure, Firebase)
• Containerised deployment (Docker)

## Conclusion

Release 4 delivers a polished, cloud‑connected IoT system with:

• Advanced telemetry
• Robust diagnostics
• Clean architecture
• Professional dashboard
• Self‑learned enhancements

## System Flowchart

Subgraph Device["Raspberry Pi (Smart Study Buddy)"]
    CAM["Camera Module"]
    TEMP["Sense HAT Temperature Sensor"]
    LED["Sense HAT LED Display"]
    MAIN["main.py (Menu + Monitoring + Health Check)"]
    CLEAN["cleanup_module.py"]
    LOG["logging_module.py"]
end

Subgraph Cloud["Adafruit IO (Cloud Dashboard)"]
    TEMP_FEED["temperature feed"]
    EVENT_FEED["events feed"]
    MON_FEED["monitoring feed"]
    STATUS_FEED["status feed"]
    LOG_FEED["logs feed"]
end

CAM --> MAIN
TEMP --> MAIN
MAIN --> LED
MAIN --> CLEAN
MAIN --> LOG

MAIN --> TEMP_FEED
MAIN --> EVENT_FEED
MAIN --> MON_FEED
MAIN --> STATUS_FEED
MAIN --> LOG_FEED

LOG --> LOG_FEED
CLEAN --> LOG_FEED

## Reference List:

Further research was completed throughout this assignment to help me get a working Study Buddy put together.
Below are lines of code I did further research on and the sites used to do so.

# MQTT Client Import

Code: import paho.mqtt.client as mqtt
Reference: https://eclipse.dev/paho/files/paho.mqtt.python/html/client.html

# SSL Module

Code: import ssl
Reference: https://docs.python.org/3/library/ssl.html

# TLS Configuration

Code: client.tls_set(cert_reqs=ssl.CERT_REQUIRED)
Code: client.tls_insecure_set(False)
Reference: https://deepwiki.eclipsesource.com/paho.mqtt.python/security-and-ssl/

# MQTT Secure Port 8883

Reference: https://docs.faircom.com/doc/ctreeedge/ctreeedge-mqtt-tls-python.htm

# Timestamp Formatting

Code: timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
Reference: https://docs.python.org/3/library/datetime.html#datetime.datetime.strftime

# Log Filename Formatting

Code: log_filename = datetime.now().strftime("logs/studybuddy_%Y-%m-%d.log")
Reference: https://docs.python.org/3/library/datetime.html#datetime.datetime.strftime

# Current Unix Time

Code: now = time.time()
Reference: https://docs.python.org/3/library/time.html#time.time

# Cutoff Time Calculation

Code: cutoff = now - (days * 24 * 60 * 60)
Reference: https://docs.python.org/3/library/time.html

# Directory Listing

Code: for filename in os.listdir(folder):
Reference: https://docs.python.org/3/library/os.html#os.listdir

# Path Joining

Code: filepath = os.path.join(folder, filename)
Reference: https://docs.python.org/3/library/os.path.html#os.path.join

# Check if Path is File

Code: if os.path.isfile(filepath):
Reference: https://docs.python.org/3/library/os.path.html#os.path.isfile

# File Modified Time

Code: file_mtime = os.path.getmtime(filepath)
Reference: https://docs.python.org/3/library/os.path.html#os.path.getmtime

# Delete File

Code: os.remove(filepath)
Reference: https://docs.python.org/3/library/os.html#os.remove

# Logging Format

Code: format="%(asctime)s - %(levelname)s - %(message)s"
Reference: https://docs.python.org/3/library/logging.html#logrecord-attributes

# Logging Level

Code: level=logging.INFO
Reference: https://docs.python.org/3/library/logging.html#logging-levels

# Stream Handler

Code: logging.StreamHandler()
Reference: https://docs.python.org/3/library/logging.handlers.html

# File Handler

Code: logging.FileHandler(log_filename)
Reference: https://docs.python.org/3/library/logging.handlers.html#filehandler

