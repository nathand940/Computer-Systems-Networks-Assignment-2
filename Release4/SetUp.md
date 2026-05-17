SETUP.md — Smart Study Buddy (Release 4)
🧩 Overview
This document explains how to set up the Smart Study Buddy Release 4 system, including hardware requirements, software installation, virtual environment setup, dependencies, and configuration steps.
It ensures the project can be reproduced on any Raspberry Pi running Python 3.11+.

🖥️ 1. System Requirements
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

🐍 2. Create and Activate the Virtual Environment
Using a virtual environment ensures all dependencies are isolated and consistent across machines.
Create the venv:
      python3 -m venv venv

Activate the venv:
      source venv/bin/activate
      
You should now see (venv) at the start of your terminal prompt.

 3. Install Required Dependencies
With the virtual environment active, install the project’s Python packages:

      pip install paho-mqtt
      pip install pillow
      pip install sense-hat
    
These packages provide:

• 	paho-mqtt → MQTT communication with Adafruit IO
• 	pillow → Image handling for the camera
• 	sense-hat → Temperature and sensor readings

 4. Configure Adafruit IO Credentials

Open the configuration file:
      nano Release4/config.py

Update the following fields with your own Adafruit IO details:
      MQTT_USERNAME = "your_username"
      MQTT_PASSWORD = "your_adafruit_io_key"

Make sure your feed names match the ones on your dashboard.

5. Enable the Raspberry Pi Camera

If using the official Pi Camera:
      sudo raspi-config

Navigate to:
      Interface Options → Legacy Camera → Enable

Reboot the Pi:
      sudo reboot

6. Test Hardware Components

Test the camera:
      rpicam-still -o test.jpg

Test the Sense HAT:
      python3 - << 'EOF'
      from sense_hat import SenseHat
      print(SenseHat().get_temperature())
      EOF

 7. Run the Smart Study Buddy System

From the project root:
      source venv/bin/activate
      python3 Release4/main.py

Use the menu to run:
• 	Health Check
• 	Monitoring Mode
• 	Cleanup
• 	View logs

8. Troubleshooting



