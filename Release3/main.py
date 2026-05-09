import time
import logging

from logging_module import setup_logging
from camera_module import capture_image
from temperature_module import read_temperature
from sensehat_module import show_message, clear_display
from cleanup_module import cleanup_old_files

def capture_image_option():
    filename = capture_image()
    if filename:
        show_message("Image captured", text_colour=(0, 255, 0))
    else:
        show_message("Image failed", text_colour=(255, 0, 0))

def read_temperature_option():
    temp = read_temperature()
    if temp is not None:
        msg = f"Temp: {temp}C"
        show_message(msg, text_colour=(0, 0, 255))
    else:
        show_message("Temp error", text_colour=(255, 0, 0))

def monitoring_mode_option():
    """
    Run a simple monitoring mode:
    - 5 cycles
    - Each cycle: capture image + read temperature
    - 10 seconds between cycles
    """
    cycles = 5
    delay = 10  # seconds

    logging.info("Starting monitoring mode.")
    show_message("Monitoring", text_colour=(255, 255, 0))

    for i in range(1, cycles + 1):
        logging.info(f"Monitoring cycle {i}/{cycles}")

        filename = capture_image()
        temp = read_temperature()

        if filename and temp is not None:
            logging.info(f"Cycle {i}: Image={filename}, Temp={temp}C")
        else:
            logging.warning(f"Cycle {i}: Issue with image or temperature.")

        time.sleep(delay)

    show_message("Monitoring done", text_colour=(0, 255, 0))
    logging.info("Monitoring mode finished.")

def view_logs_hint():
    """
    Just tells the user where logs are stored.
    """
    print("\nLogs are stored in the 'logs/' folder.")
    print("You can view them with:  cat logs/<logfilename>\n")
    show_message("Check logs folder", text_colour=(0, 255, 255))

def cleanup_option():
    """
    Cleanup old images and logs.
    """
    print("\nCleaning up old files...")
    cleanup_old_files("images", days=7)
    cleanup_old_files("logs", days=14)
    show_message("Cleanup done", text_colour=(0, 255, 0))

def print_menu():
    print("\n=== Smart Study Buddy - Release 3 ===")
    print("1. Capture an image")
    print("2. Read temperature")
    print("3. Run monitoring mode")
    print("4. View logs info")
    print("5. Cleanup old files")
    print("6. Exit")

def main():
    setup_logging()
    logging.info("Smart Study Buddy - Release 3 started.")
    clear_display()

    while True:
        print_menu()
        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            capture_image_option()
        elif choice == "2":
            read_temperature_option()
        elif choice == "3":
            monitoring_mode_option()
        elif choice == "4":
            view_logs_hint()
        elif choice == "5":
            cleanup_option()
        elif choice == "6":
            logging.info("Exiting program.")
            clear_display()
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")
            show_message("Invalid choice", text_colour=(255, 0, 0))

        time.sleep(1)

if __name__ == "__main__":
    main()
