# Release 2 — Temperature + Camera Capture (Enhanced)

## Overview
Release 2 expands the Smart Study Buddy system by introducing a **second input source** (Pi Camera) and adding more advanced processing features.
This release demonstrates clear progression from Release 1 by incorporating:

- Multi‑sensor input (SenseHAT + Camera)
- File creation and management
- Automated cleanup of old data
- LED matrix feedback
- More complex program logic

These additions strengthen the system’s functionality and align with the assignment’s requirement for increased complexity in each release.

---

## Features

### Multi‑Sensor Input
- Reads temperature from the SenseHAT
- Captures images using the Raspberry Pi Camera Module

### File Output & Management
- Saves each image with a **counter‑based filename**:
  - `image_001.jpg`
  - `image_002.jpg`
  - `image_003.jpg`
- Automatically deletes images older than a set time (e.g., 1 minute)

### Visual Feedback
- LED matrix displays **"IMG"** each time a photo is captured
- Terminal prints temperature and saved image name

### Continuous Operation
- Runs in a loop, capturing images and cleaning up old ones
- Demonstrates real‑time monitoring behaviour

---

## Requirements

### Hardware
- Raspberry Pi 4 Model B
- SenseHAT
- Raspberry Pi Camera Module (V2 or HQ Camera)

### Software
- Python 3
- SenseHAT library
- **libcamera** tools (required for Raspberry Pi OS Bullseye/Bookworm)

Install libcamera:

sudo apt update
sudo apt install -y libcamera-apps

---

## How to Run
1. 	Navigate to the Release 2 folder:
        cd Release2
2. 	Run the script:
        python3 camera_capture.py
3. 	Expected behaviour:
• 	Temperature printed to the terminal
• 	A new image saved every loop
• 	LED matrix scrolls "IMG"
• 	Old images automatically deleted
• 	Filenames increment (001, 002, 003…)

Press CTRL + C to stop the program.
