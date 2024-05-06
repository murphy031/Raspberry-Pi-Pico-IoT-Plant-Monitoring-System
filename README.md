# Temp-Humidity-Pressure-Moisture-sensor-Raspberry-Pi-Pico

IoT Plant Monitoring System
This repository contains code for an IoT plant monitoring system using MicroPython and various sensors. The system collects temperature, humidity, pressure, and moisture level data from sensors and displays it on OLED screens. Additionally, it sends this data to a server for further analysis or monitoring.

Hardware Components Used
Raspberry Pi Pico microcontroller
BME280 sensor for temperature, humidity, and pressure
Moisture sensor
SSD1306 OLED displays (two displays used in this project)
WiFi connection (if available, can be omitted if not needed)
Setup Instructions
Connect the hardware components according to the wiring specified in the code.
Flash MicroPython firmware to your Raspberry Pi Pico microcontroller.
Upload the Python scripts (main.py) to the microcontroller.
Modify the script with your WiFi credentials (WIFI_SSID and WIFI_PASSWORD) if you're using WiFi.
Ensure that the server endpoint (http://yourwebsite.com/route) matches your server setup. You may need to adjust this URL to fit your specific server configuration.
Power on the device, and it will automatically start collecting sensor data.
Usage
Once the system is set up and running:

Sensor data (temperature, humidity, pressure, and moisture level) will be displayed on the OLED screens.
The moisture level will determine the facial expression displayed on one of the OLED screens (smiley or frowny face).
Sensor data will be sent to the specified server endpoint via HTTP POST requests in JSON format.
The system will handle exceptions during sensor readings and continue operation.
Notes
If you're not using WiFi, you can omit the WiFi connection part from the script.
Ensure that the server endpoint is accessible and configured to receive data in JSON format.
Adjust the sleep time (sleep(30)) in the script to change the interval between sensor readings and data transmissions.
Dependencies
MicroPython firmware
BME280 library
ssd1306 library
urequests library (for HTTP requests)
License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments
This project was inspired by the need for a simple and efficient plant monitoring system.
Thanks to the contributors of the MicroPython, BME280, and ssd1306 libraries for their valuable work.
