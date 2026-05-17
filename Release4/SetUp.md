# SETUP.md — Smart Study Buddy (Release 4)

# Overview

This document explains how to set up the Smart Study Buddy Release 4 system, including hardware requirements, software installation, virtual environment setup, dependencies, and configuration steps.

It ensures the project can be reproduced on any Raspberry Pi running Python 3.11+.

# 1. System Requirements

Hardware
• 	Raspberry Pi (3B, 4B, or Zero 2 W recommended)
• 	Sense HAT (or Sense HAT emulator for testing)
• 	Raspberry Pi Camera Module (or compatible USB camera)
• 	MicroSD card with Raspberry Pi OS (Bookworm)
• 	Internet connection (Wi‑Fi or Ethernet)

Software
• 	Raspberry Pi OS (Bookworm)
• 	Python 3.11+
• 	Adafruit IO account (for MQTT dashboard)
• 	MQTT over TLS support (included with Python’s  module)

# 2. Create and Activate the Virtual Environment

Using a virtual environment ensures all dependencies are isolated and consistent across machines.
Create the venv:
      python3 -m venv venv

Activate the venv:
      source venv/bin/activate
      
You should now see (venv) at the start of your terminal prompt.

# 3. Install Required Dependencies

With the virtual environment active, install the project’s Python packages:

      pip install paho-mqtt
      pip install pillow
      pip install sense-hat
    
These packages provide:

• 	paho-mqtt → MQTT communication with Adafruit IO
• 	pillow → Image handling for the camera
• 	sense-hat → Temperature and sensor readings

# 4. Configure Adafruit IO Credentials

Open the configuration file:
      nano Release4/config.py

Update the following fields with your own Adafruit IO details:
      MQTT_USERNAME = "your_username"
      MQTT_PASSWORD = "your_adafruit_io_key"

Make sure your feed names match the ones on your dashboard.

# 5. Enable the Raspberry Pi Camera

If using the official Pi Camera:
      sudo raspi-config

Navigate to:
      Interface Options → Legacy Camera → Enable

Reboot the Pi:
      sudo reboot

# 6. Test Hardware Components

Test the camera:
      rpicam-still -o test.jpg

Test the Sense HAT:
      python3 - << 'EOF'
      from sense_hat import SenseHat
      print(SenseHat().get_temperature())
      EOF

# 7. Run the Smart Study Buddy System

From the project root:
      source venv/bin/activate
      python3 Release4/main.py

Use the menu to run:
• 	Health Check
• 	Monitoring Mode
• 	Cleanup
• 	View logs

# 8. Troubleshooting

This section lists common issues you may encounter when running the Smart Study Buddy system and how to resolve them.

# MQTT Not Connecting
 
Symptoms:
• 	“Failed to connect to MQTT broker”
• 	Dashboard not updating

Fixes:
• 	Check your Adafruit IO username and key in 
• 	Ensure your device has internet access
• 	Confirm port 8883 is used (TLS required)
• 	Make sure the virtual environment is activated before running

# Camera Not Capturing Images

Symptoms:
• 	Blank images
• 	“Camera error” in Health Check
• 	No new files in

Fixes:
• 	Ensure the Raspberry Pi Camera is enabled in raspi-config
• 	Check that the camera ribbon cable is fully seated
• 	Test manually:
           rpicam-still -o test.jpg

# Sense HAT Not Reading Temperature

Symptoms:
• 	Temperature always 0
• 	“Temperature sensor error” in Health Check

Fixes:
• 	Ensure the Sense HAT is firmly attached
• 	Install the library inside the venv:
           pip install sense-hat
• 	Reboot the Pi to reload I2C drivers

# Logs Not Being Created

Symptoms:
• 	No files in logs/
• 	Logging output missing

Fixes:
• 	Ensure the logs/ folder exists
• 	Check file permissions
• 	Verify the logging path in logging_module.py

# Cleanup Not Removing Files

Symptoms:
• 	Old images remain in the folder
• 	“0 files removed” message

Fixes:
• 	Check the  value in the cleanup function
• 	Ensure file timestamps are correct
• 	Confirm the script has permission to delete files

# Virtual Environment Issues

Symptoms:
• 	“Module not found” errors
• 	MQTT or Sense HAT imports failing

Fixes:
• Activate the venv before running the program:
         source venv/bin/activate
• Reinstall dependencies if needed:
         pip install paho-mqtt pillow sense-hat

# Dashboard Not Updating

Symptoms:
• 	Feeds not changing
• 	No new entries in Adafruit IO

Fixes:
• 	Check MQTT connection status
• 	Ensure feed names in mqtt_module.py match your dashboard
• 	Refresh the dashboard page
• 	Verify your Adafruit IO key is correct


