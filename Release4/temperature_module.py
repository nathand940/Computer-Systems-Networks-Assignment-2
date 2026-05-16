from mqtt_module import publish_log # Cloud log feed for temperature events
from mqtt_module import publish_temperature # Cloud temperature feed
from sense_hat import SenseHat # Sense HAT hardware interface
import logging # Local logging system
import time # Used to attach timestamps to MQTT messages

sense = SenseHat() # Create a single Sense HAT instance for reading sensor data

def read_temperature():
    """
    Read temperature from the Sense HAT and return it in Celsius (rounded).
    """
    try:
        temp = sense.get_temperature() # Read raw temperature value from the Sense HAT sensor
        temp = round(temp, 1) # Round to 1 decimal place for cleaner output
        logging.info(f"Temperature read: {temp} °C") # Log the reading to the local log file
        publish_log(f"Temperature read: {temp}C") # Publish a human-readable log message to the cloud logs feed
        publish_temperature(f"{temp},{int(time.time())}") # Publish temperature + timestamp to the cloud temperature feet with format: "<temp>,<unix_timestamp>"
        return temp
    except Exception as e:
        logging.error(f"Error reading temperature: {e}") # Catch unexpected hardware or read errors
        return None
