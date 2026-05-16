from mqtt_module import publish_log # Cloud log feed for cleanup events
from mqtt_module import publish_event # Cloud event feed (used when cleanup deletes files)
import os # File and directory operations
import time # Used to calculate file age
import logging # Local logging system

def cleanup_old_files(folder, days=7):
    """
    Delete files in 'folder' older than 'days' days.
    """
    if not os.path.isdir(folder): # Ensure the folder exists before attempting cleanup
        logging.warning(f"Cleanup skipped: folder '{folder}' does not exist.")
        return

    now = time.time() # Current time in seconds
    cutoff = now - (days * 24 * 60 * 60) # Convert days → seconds to calculate age limit

    deleted_count = 0 # Track how many files were removed. Counter initialised

    for filename in os.listdir(folder):
        filepath = os.path.join(folder, filename) # Loop through all files in the folder

        if os.path.isfile(filepath): # Only process actual files (ignore subfolders)
            file_mtime = os.path.getmtime(filepath) # Last modified time of the file
            if file_mtime < cutoff: # If file is older than the cutoff, delete it
                try:
                    os.remove(filepath)
                    deleted_count += 1
                    logging.info(f"Deleted old file: {filepath}")
                except Exception as e:
                    logging.error(f"Error deleting file {filepath}: {e}")

    logging.info(f"Cleanup complete in '{folder}'. Files deleted: {deleted_count}") # Log summary of cleanup
    publish_log(f"Cleanup executed in '{folder}', deleted {deleted_count} files") # Publish cleanup summary to cloud logs
    if deleted_count > 0:
       publish_event(f"cleanup_completed:{folder}:{deleted_count}") # Publish a cloud event only if files were actually deleted



