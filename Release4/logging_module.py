import logging # Python's built‑in logging framework
import os # Used to create the logs directory
from datetime import datetime # Used to generate daily log filenames

def setup_logging():
    # Ensure logs directory exists
    os.makedirs("logs", exist_ok=True)

    # Log file name with date
    log_filename = datetime.now().strftime("logs/studybuddy_%Y-%m-%d.log") # Generate a log filename based on the current date

    logging.basicConfig(
        level=logging.INFO, # INFO captures normal events + warnings + errors
        format="%(asctime)s - %(levelname)s - %(message)s", # Format includes timestamp, log level, and message
        handlers=[
            logging.FileHandler(log_filename), # FileHandler writes logs to the daily file
            logging.StreamHandler() #StreamHandler prints logs to the terminal
        ]
    )

    logging.info("Logging initialised.")
