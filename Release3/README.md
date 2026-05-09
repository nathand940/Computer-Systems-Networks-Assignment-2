Release 3 – Smart Study Buddy
Integrated Monitoring System with Modular Design, Logging, Menu Interface & Automated Cleanup

## 1. Overview

## Release 3 represents the final and most advanced stage of the Smart Study Buddy project.
This release integrates all previous functionality (temperature sensing, image capture, Sense HAT feedback) into a modular, menu‑driven monitoring system with:
• 	A structured multi‑module Python architecture
• 	A user‑friendly terminal menu
• 	Automated logging
• 	Monitoring mode (periodic capture + temperature readings)
• 	Automated cleanup of old images and logs
• 	Improved error handling and system reliability
This release demonstrates professional software engineering practices, including modularity, maintainability, and clear separation of concerns.

## 2. New Features in Release 3

## Release 3 introduces several major enhancements: Modular Python Architecture

The system is now split into dedicated modules:

• Main.py - Central controller + menu system
• Camera_Module.py - Image capture using rpicam-still
• Temperature_Module.py - Temperature readings from Sense HAT
• SenseHat_Module.py - LED display messaging
• Logging_Moudle.py - Centralised logging configuration
• CleanUp_Module.py - Automated deletion of old files

This structure improves readability, maintainability, and professional quality.

## Menu‑Driven User Interface

Users interact with the system through a clear terminal menu:

   1. Capture an image
   2. Read temperature
   3. Run monitoring mode
   4. View logs info
   5. Cleanup old files
   6. Exit

This makes the system easy to demonstrate and intuitive to use.

## Monitoring Mode

A fully automated monitoring cycle:

• Captures an image
• Reads temperature
• Logs both
• Repeats for 5 cycles
• 10‑second delay between cycles

This simulates a real monitoring system.

## Automated Logging

All system activity is logged to:

• logs/studybuddy_YYYY-MM-DD.log

Logged events include:

• Image captures
• Temperature readings
• Monitoring cycles
• Cleanup actions
• Errors and exceptions

This provides traceability and evidence.

## Automated Cleanup

Old files are automatically removed:

• Images older than 7 days
• Logs older than 14 days

This prevents storage bloat and demonstrates lifecycle management.

## 3. Folder Structure

Release 3 uses the following directory layout:

Release3/
│
├── main.py
├── camera_module.py
├── temperature_module.py
├── sensehat_module.py
├── logging_module.py
├── cleanup_module.py
├── images/        # Captured photos stored here
└── logs/          # Daily log files stored here

This structure separates logic, data, and output clearly.

## 4. How to Run Release 3

Step 1 — Navigate to Release 3:

• cd ~/Computer-Systems-Networks-Assignment-2/Release3

Step 2 — Run the main program:

• python3 main.py

Step 3 — Use the menu:

• Choose any option by entering its number.

## 5. Dependencies

Release 3 requires the following packages:

• Python 3
• Rpicam-apps (for camera capture)
• Sense-hat (for temperature + LED display)

Install with:

• sudo apt install -y rpicam-apps sense-hat

Python Standard Library Modules Used:

• Logging
• Subprocess
• OS
• Time
• DateTime

No external Python packages are required.

## 6. Detailed Module Descriptions
6.1 Main.py:

• Provides the menu interface
• Calls functions from all other modules
• Controls program flow
• Handles user input
• Displays Sense HAT messages
• Logs all actions

6.2 Camera_Module.py:

• Captures images using:

     • rpicam-still -o <filename> -n

• Automatically timestamps filenames
• Saves images to images/
• Logs success or failure

6.3
 
• Reads temperature from the Sense HAT
• Rounds to 1 decimal place
• Logs the reading
• Returns None on failure

6.4
 
• Displays scrolling messages
• Clears the LED matrix
• Handles display errors gracefully

6.5 

• Creates daily log files
• Logs to both file and console
• Ensures logs directory exists
• Used by all modules

6.6 

• Deletes files older than a specified number of days
• Used for both images and logs
• Logs each deletion

##7. Testing and Verification

Image Capture Test:

• Select menu option 1
• Confirm a new file appears in images/
• Check log file for confirmation

Temperature Test:

• Select menu option 2
• Sense HAT displays temperature
• Log file records reading

Monitoring Mode Test:

• Select menu option 3
• System runs 5 cycles
• Images + logs generated automatically

Cleanup Test:

• Select menu option 5
• Old files removed
• Log file records deletions

## 8. Challenges and Solutions

Camera compatibility on Bookworm:

• Bookworm uses libcamera instead of raspistill.
• Solution: switched to rpicamstill and updated all capture logic.

• SSH host key mismatch after OS reinstall
• Solution: removed old key using:
    • ssh-keygen -R hdiprpi.local

Ensuring modularity:

• Separated all functionality into dedicated modules to improve clarity and maintainability.

Automated logging:

• Implemented a central logging system to track all events and errors.

## 9. Conclusion

Release 3 completes the Smart Study Buddy system by integrating all features into a polished, modular, and user‑friendly application.

This release demonstrates:
• Professional software structure
• Robust error handling
• Automated monitoring
• Logging and cleanup
• Clear user interaction

It represents a fully functional IoT‑style monitoring system suitable for academic assessment and real‑world extension.
