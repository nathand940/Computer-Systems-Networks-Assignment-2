# Release 1 — Basic Environment Monitor
Part of the *Smart Study Buddy — Camera‑Assisted Productivity Environment Monitor* project.

## Overview
Release 1 delivers the **minimum viable prototype** of the Smart Study Buddy system.  
This release focuses on a single input source and a simple one‑way data flow:

**SenseHAT Temperature Sensor → Raspberry Pi → Console Output + LED Matrix Feedback**

The purpose of this release is to demonstrate:
- Basic hardware interaction  
- Simple data processing  
- Clear visual and textual output  

This fully satisfies the Release 1 requirements of the assignment.

---

## Features
- Reads temperature from the SenseHAT sensor  
- Prints the current temperature to the terminal  
- Displays a colour on the LED matrix to indicate comfort level:
  - **Blue** — Too cold  
  - **Green** — Comfortable  
  - **Red** — Too warm  

This establishes the foundation for later releases, where additional sensors, camera input, networking, and cloud integration will be added.

---

## Hardware & Software Requirements
- Raspberry Pi 3 or 4  
- SenseHAT attached to the GPIO header  
- Python 3  
- SenseHAT Python library (`sense-hat`)  

Install the library if needed:

sudo apt update

sudo apt install sense-hat -y

---

## How to Run the Script

1. 	Navigate to the Release 1 directory:

    - cd Release1

2. 	Run the temperature monitor:

    - python3 temp_monitor.py

3. 	Expected behaviour:

  	- Temperature readings appear in the terminal
  	- LED matrix changes colour based on the temperature

4.  Stop Script:

    - Press CTRL + C to stop the script.

## What This Release Demonstrates:

-   One real input source (SenseHAT temperature sensor)
- 	Basic one‑way connection (sensor → device output)
- 	Two programme strands:
    - 	 Programming (Python)
    -    Computer systems/hardware (Raspberry Pi + SenseHAT)
-   Minimal communication resources:
    -  	 This README
    -  	 A short demo video (provided during submission)

Release 1 forms the foundation for Release 2, where additional functionality such as camera input or networking will be introduced.
