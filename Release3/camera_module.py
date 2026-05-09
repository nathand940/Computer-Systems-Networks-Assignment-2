import subprocess
import os
from datetime import datetime
import logging

def capture_image():
    """
    Capture an image using rpicam-still and save it in the images/ folder.
    Returns the filename if successful, else None.
    """
    try:
        os.makedirs("images", exist_ok=True)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"images/image_{timestamp}.jpg"

        logging.info(f"Capturing image to {filename}")

        result = subprocess.run(
            ["rpicam-still", "-o", filename, "-n"],
            capture_output=True,
            text=True
        )

        if result.returncode == 0:
            logging.info(f"Image captured successfully: {filename}")
            return filename
        else:
            logging.error(f"rpicam-still failed: {result.stderr}")
            return None

    except Exception as e:
        logging.error(f"Error capturing image: {e}")
        return None
