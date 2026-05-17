## Reference List - Study Buddy (Release4):

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

# Creating Virtual Enviornment

Code: python3 -m venv venv/source venv/bin/activate
Reference: https://docs.python.org/3/library/venv.html
