# Raspberry Pi Motion Capture Project

This project implements a motion capture system using a PIR motion sensor, a Raspberry Pi Camera, and a Raspberry Pi. The code is organized into two main components: the motion capture system and the web server. The functionality is detailed below.

---

## Project Overview

### 1. **Motion Capture System**
The main code manages the motion detection and photo capture process. Key features include:

- **Motion Detection**:
    -The PIR motion sensor detects motion.
    -If motion is detected for at least 2 seconds, and then stops, the system captures an image.

- **Image Capture and Storage**:
    -The Raspberry Pi Camera captures a photo whenever motion is detected.
    -Each photo is saved with a timestamp in the filename to ensure unique names and prevent overwriting.

- **Log File Maintenance**:
    -A log file records the details of all captured photos, including their timestamps.
    -This log helps track the total number of images captured and provides an overview of motion events.

- **Email Notifications**:
    -All captured photos are sent via email for remote access and monitoring

### 2. **Web Server**

A Flask-based web server has been implemented to provide remote access to the motion capture data. Features include:

- **Photo Overview**:
    -Displays the total number of photos taken since the last refresh or login.
    -Shows the latest photo captured by the system.

- **User Interface**:
    -Accessible through a provided URL.
    -Simple and user-friendly layout for monitoring captured images and system activity.


### **Prerequisites**

- **Hardware Requirements**:
    -Raspberry Pi (any compatible model).
    -PIR motion sensor.
    -Raspberry Pi Camera Module.

- **Software Requirements**:
    -Python 3.
    -Flask library.
    -SMTP setup for email functionality.
