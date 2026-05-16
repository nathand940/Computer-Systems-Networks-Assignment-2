# config.py
# Stores MQTT credentials and topic names for Release 4

MQTT_BROKER = "io.adafruit.com" # Adafruit IO hostname
MQTT_PORT = 8883  # TLS port for secure MQTT

MQTT_USERNAME = "Nathand940"
MQTT_PASSWORD = "aio_nUvs86hrDG1SvAZbPc41E47BIQzP"

# ---------------------------------------------------------
# MQTT TOPIC MAPPINGS
# ---------------------------------------------------------
# These map friendly names (keys) to the actual MQTT feed paths.
# The rest of the system uses the keys (e.g., "temperature"),
# and mqtt_module.py converts them into full topic strings.

MQTT_TOPICS = {
    "temperature": "Nathand940/feeds/temperature", # Temperature readings + timestamps
    "event": "Nathand940/feeds/events", # System events (image captured, motion, etc.)
    "status": "Nathand940/feeds/status", # Online/offline status messages
    "monitoring": "Nathand940/feeds/monitoring", # Monitoring cycle start/end events
    "logs": "Nathand940/feeds/logs" # Cloud log messages for Release 4

}
