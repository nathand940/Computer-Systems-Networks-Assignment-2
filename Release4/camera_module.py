import subprocess # Used to run external commands like rpicam-still
import os # Used for directory creation and file handling

from mqtt_module import publish_event # Sends cloud events when images are captured
from datetime import datetime # Used to generate timestamped filenames
import logging # Logs image capture activity to local log files

def capture_image():
    """
    Capture an image using rpicam-still and save it in the images/ folder.
    Returns the filename if successful, else None.
    """
    try:
        os.makedirs("images", exist_ok=True) # Ensure the images/ directory exists (creates it if missing)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S") # Generate a timestamped filename to avoid overwriting images
        filename = f"images/image_{timestamp}.jpg"

        logging.info(f"Capturing image to {filename}") # Log the capture attempt

        result = subprocess.run( # Run the rpicam-still command to capture the image
            ["rpicam-still", "-o", filename, "-n"], # -o <file>: output file / -n: no preview window
            capture_output=True, # Capture stdout/stderr for debugging
            text=True # Return output as text instead of bytes
        )

        if result.returncode == 0:
            logging.info(f"Image captured successfully: {filename}")
            publish_event(f"image_captured:{filename}") # Cloud event for dashboard
            return filename
        else:
            logging.error(f"rpicam-still failed: {result.stderr}") # Log the error output from rpicam-still
            return None

    except Exception as e:
        logging.error(f"Error capturing image: {e}") # Catch unexpected errors such as "camera not detected"
        return None
