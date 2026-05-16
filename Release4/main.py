import os # Gives access to functions that interact with the Raspberry Pi
import time # Provides functions for working with time, delays, and timestamps
import logging # Enables Python’s built‑in logging system

# Import MQTT publishing functions for monitoring, status updates, and cloud logs

from mqtt_module import publish_monitoring
from mqtt_module import connect_mqtt, publish_status
from mqtt_module import publish_log

# Import local logging setup

from logging_module import setup_logging

# Import hardware interaction modules

from camera_module import capture_image
from temperature_module import read_temperature
from sensehat_module import show_message, clear_display

# Import cleanup functionality

from cleanup_module import cleanup_old_files

connect_mqtt() # Connect to the MQTT broker at program start
publish_status("online") # Publish system status to cloud dashboard

def capture_image_option():
    filename = capture_image() # Attempt to capture an image
    if filename:
        publish_log(f"Image captured: {filename}") # Log success to cloud
        show_message("Image captured", text_colour=(0, 255, 0)) # Green success message
    else:
        show_message("Image failed", text_colour=(255, 0, 0)) # Red error message

def read_temperature_option():
    temp = read_temperature()  # Get temperature value
    if temp is not None:
        publish_log(f"Temperature read: {temp}C") # Log success to cloud
        msg = f"Temp: {temp}C"
        show_message(msg, text_colour=(0, 0, 255)) # Blue message for temperature
    else:
        show_message("Temp error", text_colour=(255, 0, 0)) # Red error message

def monitoring_mode_option():
    """
    Run a simple monitoring mode:
    - 5 cycles
    - Each cycle: capture image + read temperature
    - 10 seconds between cycles
    """
    cycles = 5 # number of cycles to be completed
    delay = 10  # seconds between cycles

    logging.info("Starting monitoring mode.")
    publish_log("Monitoring mode started") # Cloud log entry
    show_message("Monitoring", text_colour=(255, 255, 0)) # Yellow LED message

    for i in range(1, cycles + 1):
        publish_monitoring(f"cycle_{i}_started") # Cloud event for cycle start
        logging.info(f"Monitoring cycle {i}/{cycles}")

        filename = capture_image() # Capture image
        temp = read_temperature() # Read temperature

        if filename and temp is not None:
            logging.info(f"Cycle {i}: Image={filename}, Temp={temp}C")
        else:
            logging.warning(f"Cycle {i}: Issue with image or temperature.")

        time.sleep(delay) # Wait before next cycle
        publish_monitoring(f"cycle_{i}_completed") # Cloud event for cycle completion
        publish_log(f"Monitoring cycle {i} completed") # Cloud log entry

    show_message("Monitoring done", text_colour=(0, 255, 0)) # Green success message
    logging.info("Monitoring mode finished.")
    publish_log("Monitoring mode finished")
    publish_monitoring("all_cycles_completed") # Final cloud event


def view_logs_hint():
    """
    Just tells the user where logs are stored.
    """
    print("\nLogs are stored in the 'logs/' folder.")
    print("You can view them with:  cat logs/<logfilename>\n")
    show_message("Check logs folder", text_colour=(0, 255, 255)) # cyan success message

def cleanup_option():
    """
    Cleanup old images and logs.
    """
    print("\nCleaning up old files...")
    cleanup_old_files("images", days=7) # Delete images older than 7 days
    cleanup_old_files("logs", days=14) # Delete logs older than 14 days
    publish_log("Cleanup executed") # Cloud log entry
    show_message("Cleanup done", text_colour=(0, 255, 0)) # Green success message

def health_check_option():
    print("\n=== Running System Health Check ===")
    show_message("Health Check", text_colour=(0, 255, 255))

    results = [] # Store results for terminal output

    # --- Camera Test ---
    try:
        test_filename = capture_image()
        if test_filename:
            results.append("Camera: OK")
            publish_log("HealthCheck: Camera OK")
        else:
            results.append("Camera: FAIL")
            publish_log("HealthCheck: Camera FAIL")
    except Exception as e: #catches errors
        results.append(f"Camera: ERROR ({e})")
        publish_log(f"HealthCheck: Camera ERROR {e}")

    # --- Temperature Test ---
    try:
        temp = read_temperature()
        if temp is not None:
            results.append(f"Temperature Sensor: OK ({temp}C)")
            publish_log("HealthCheck: Temperature OK")
        else:
            results.append("Temperature Sensor: FAIL")
            publish_log("HealthCheck: Temperature FAIL")
    except Exception as e: #catches errors
        results.append(f"Temperature Sensor: ERROR ({e})")
        publish_log(f"HealthCheck: Temperature ERROR {e}")

    # --- MQTT Test ---
    try:
        publish_log("HealthCheck: MQTT Test Message")
        results.append("MQTT: OK") # If this succeeds, MQTT is working

    except Exception as e: #catches errors
        results.append(f"MQTT: ERROR ({e})")

    # --- Disk Space Test ---
    try:
        stat = os.statvfs("/") #Get filesystem statistics for the SD card
        free_mb = (stat.f_bavail * stat.f_frsize) / (1024 * 1024) # Multiplies Number of free blocks available by Size of each block in bytes to get total number of bytes then converts them to MB
        results.append(f"Disk Space: {free_mb:.1f} MB free")
        publish_log(f"HealthCheck: Disk {free_mb:.1f}MB free")
    except Exception as e: #catches errors
        results.append(f"Disk Space: ERROR ({e})")
        publish_log(f"HealthCheck: Disk ERROR {e}")

    # --- Print results ---
    print("\nHealth Check Results:")
    for r in results:
        print(" - " + r)

    show_message("Health Check Done", text_colour=(0, 255, 0)) # Green success message
    print()

def print_menu():
    print("\n=== Smart Study Buddy - Release 3 ===")
    print("1. Capture an image")
    print("2. Read temperature")
    print("3. Run monitoring mode")
    print("4. View logs info")
    print("5. Cleanup old files")
    print("6. Health check")
    print("7. Exit")

def main():
    setup_logging() # Initialise local logging system
    logging.info("Smart Study Buddy - Release 3 started.")
    publish_log("System started") # Cloud log entry
    clear_display() # Clear LED matrix at startup

    while True:
        print_menu()
        choice = input("Enter your choice (1-6): ").strip() # Looks for user input

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
             health_check_option()
        elif choice == "7":
            logging.info("Exiting program.")
            publish_log("System shutting down")
            publish_status("offline") # Update cloud dashboard
            clear_display()
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")
            show_message("Invalid choice", text_colour=(255, 0, 0))

        time.sleep(1) # Small delay for smoother UX


if __name__ == "__main__":
    main()
