from sense_hat import SenseHat
import time
import subprocess
from datetime import datetime, timedelta
import os

sense = SenseHat()

# Create images directory if it doesn't exist
if not os.path.exists("images"):
    os.makedirs("images")

# How long to keep images (in minutes)
IMAGE_LIFETIME_MINUTES = 5  # change this to whatever you want

# Function to get the next image number
def get_next_image_number():
    files = [f for f in os.listdir("images") if f.startswith("image_") and f.endswith(".jpg")]
    if not files:
        return 1
    numbers = []
    for f in files:
        try:
            num = int(f.split("_")[1].split(".")[0])
            numbers.append(num)
        except:
            pass
    return max(numbers) + 1 if numbers else 1

# Function to delete old images
def cleanup_old_images():
    now = datetime.now()
    cutoff = now - timedelta(minutes=IMAGE_LIFETIME_MINUTES)

    for filename in os.listdir("images"):
        filepath = os.path.join("images", filename)
        if os.path.isfile(filepath):
            file_time = datetime.fromtimestamp(os.path.getmtime(filepath))
            if file_time < cutoff:
                os.remove(filepath)
                print(f"Deleted old image: {filename}")

while True:
    # Read temperature
    temp = round(sense.get_temperature(), 1)
    print(f"Temperature: {temp} °C")

    # Determine next image number
    image_number = get_next_image_number()
    filename = f"images/image_{image_number:03d}.jpg"

    # Capture image
    subprocess.run(["libcamera-still", "-o", filename])
    print(f"Image saved: {filename}")

    # LED feedback
    sense.show_message("IMG", scroll_speed=0.05)

    # Cleanup old images
    cleanup_old_images()

    time.sleep(5)
