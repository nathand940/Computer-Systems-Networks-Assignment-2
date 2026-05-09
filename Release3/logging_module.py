import logging
import os
from datetime import datetime

def setup_logging():
    # Ensure logs directory exists
    os.makedirs("logs", exist_ok=True)

    # Log file name with date
    log_filename = datetime.now().strftime("logs/studybuddy_%Y-%m-%d.log")

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[
            logging.FileHandler(log_filename),
            logging.StreamHandler()
        ]
    )

    logging.info("Logging initialised.")
