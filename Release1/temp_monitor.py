from sense_hat import SenseHat
import time

sense = SenseHat()

# Define some colours
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Simple comfort thresholds (you can tweak these)
COMFORT_MIN = 18.0   # degrees C
COMFORT_MAX = 24.0   # degrees C

while True:
    temp = sense.get_temperature()
    temp = round(temp, 1)

    print(f"Current temperature: {temp} °C")

    # Decide LED colour based on temperature
    if temp < COMFORT_MIN:
        colour = BLUE      # too cold
    elif temp > COMFORT_MAX:
        colour = RED       # too warm
    else:
        colour = GREEN     # comfortable

    # Fill the LED matrix with the chosen colour
    sense.clear(colour)

    # Wait a bit before next reading
    time.sleep(2)
