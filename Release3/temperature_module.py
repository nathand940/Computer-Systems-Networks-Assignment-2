from sense_hat import SenseHat
import logging

sense = SenseHat()

def read_temperature():
    """
    Read temperature from the Sense HAT and return it in Celsius (rounded).
    """
    try:
        temp = sense.get_temperature()
        temp = round(temp, 1)
        logging.info(f"Temperature read: {temp} °C")
        return temp
    except Exception as e:
        logging.error(f"Error reading temperature: {e}")
        return None
