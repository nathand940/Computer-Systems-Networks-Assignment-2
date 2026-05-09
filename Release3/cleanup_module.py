import os
import time
import logging

def cleanup_old_files(folder, days=7):
    """
    Delete files in 'folder' older than 'days' days.
    """
    if not os.path.isdir(folder):
        logging.warning(f"Cleanup skipped: folder '{folder}' does not exist.")
        return

    now = time.time()
    cutoff = now - (days * 24 * 60 * 60)

    deleted_count = 0

    for filename in os.listdir(folder):
        filepath = os.path.join(folder, filename)

        if os.path.isfile(filepath):
            file_mtime = os.path.getmtime(filepath)
            if file_mtime < cutoff:
                try:
                    os.remove(filepath)
                    deleted_count += 1
                    logging.info(f"Deleted old file: {filepath}")
                except Exception as e:
                    logging.error(f"Error deleting file {filepath}: {e}")

    logging.info(f"Cleanup complete in '{folder}'. Files deleted: {deleted_count}")
