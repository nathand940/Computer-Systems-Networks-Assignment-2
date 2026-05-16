# mqtt_module.py
# Handles MQTT connection and publishing for Release 4
# Smart Study Buddy – Nathan Dolan

import paho.mqtt.client as mqtt # MQTT client library for connecting + publishing
import ssl # Provides TLS/SSL encryption support
import time # Used for time, delays, timestamp, etc.
from config import MQTT_BROKER, MQTT_PORT, MQTT_USERNAME, MQTT_PASSWORD, MQTT_TOPICS # Import MQTT settings and topic mappings from config.py


# Create a single global MQTT client instance
client = mqtt.Client() # This client is reused for all publish operations


def connect_mqtt():
    """Connects to the MQTT broker using credentials from config.py."""
    try:
        client.username_pw_set(MQTT_USERNAME, MQTT_PASSWORD)

        # Enable TLS for secure connection (Adafruit IO)
        client.tls_set(cert_reqs=ssl.CERT_REQUIRED)
        client.tls_insecure_set(False) # Do not allow insecure certificates ensuring access to the REAL Adafruit IO

        client.connect(MQTT_BROKER, MQTT_PORT, keepalive=60)  # Connect to the broker using host + port from config.py
        client.loop_start() # Start background network loop so MQTT can send/receive messages

        print("[MQTT] Connected to broker")
        return True

    except Exception as e:
        print(f"[MQTT] Connection failed: {e}")
        return False


def publish(topic_key, message):
    """
    Publishes a message to a topic defined in config.py.
    topic_key = key from MQTT_TOPICS dict (e.g. 'temperature', 'event')
    """
    try:
        topic = MQTT_TOPICS.get(topic_key) # Look up the actual MQTT topic string using the key
        if not topic:
            print(f"[MQTT] Unknown topic key: {topic_key}") # If the key doesn't exist, warn the user
            return False

        client.publish(topic, message) # Publish the message to the resolved topic
        print(f"[MQTT] Published to {topic}: {message}")
        return True

    except Exception as e:
        print(f"[MQTT] Publish failed: {e}")
        return False


# Convenience wrappers for your system
def publish_temperature(temp):
    publish("temperature", str(temp)) # Convert to string for MQTT


def publish_event(event_name):
    publish("event", event_name) # Publish system events


def publish_status(status):
    publish("status", status) # Online/offline indicator


def publish_monitoring(message):
    publish("monitoring", message) # Monitoring cycle events

def publish_log(message):
    publish("logs", message) # Cloud log messages for Release 4

