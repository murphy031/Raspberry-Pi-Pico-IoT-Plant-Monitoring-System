from machine import Pin, I2C, ADC
from time import sleep
import BME280
from math import sin, cos, radians
from ssd1306 import SSD1306_I2C
import network
import urequests
import json

# Function to connect to Wi-Fi
def connect_wifi(ssid, password):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('Connecting to Wi-Fi...')
        wlan.connect(ssid, password)
        while not wlan.isconnected():
            pass
    print('Connected to Wi-Fi:', wlan.ifconfig())
    

WIFI_SSID = "wifi_name"
WIFI_PASSWORD = "password"
connect_wifi(WIFI_SSID, WIFI_PASSWORD)

# Initialize I2C communication for BME280 sensor
i2c_bme = I2C(id=0, scl=Pin(5), sda=Pin(4), freq=100000)
bme = BME280.BME280(i2c=i2c_bme)

# Initialize I2C communication for OLED displays
i2c_oled = I2C(id=1, scl=Pin(3), sda=Pin(2), freq=400000)
i2c_second_oled = I2C(id=0, scl=Pin(5), sda=Pin(4), freq=400000)

# Initialize pin for moisture sensor's digital output (DO)
adc = ADC(Pin(26))

# Define the maximum and minimum moisture sensor readings
MAX_MOISTURE_READING = 65535
MIN_MOISTURE_READING = 34000

# Initialize the first OLED display for sensor readings
oled = SSD1306_I2C(128, 64, i2c_oled)

# Initialize the second OLED display for moisture level
second_oled = SSD1306_I2C(128, 64, i2c_second_oled, 0x3C)  # Use common I2C channel with a different address

# Function to draw a half circle
def draw_half_circle(oled, x, y, r, direction):
    if direction == "up":
        start_angle = 0
        end_angle = 180
    elif direction == "down":
        start_angle = 180
        end_angle = 360

    for i in range(start_angle, end_angle, 10):
        oled.pixel(int(x + r * cos(radians(i))), int(y + r * sin(radians(i))), 1)

# Function to draw a circle
def draw_circle(oled, x, y, r):
    for i in range(0, 360, 5):
        oled.pixel(int(x + r * cos(radians(i))), int(y + r * sin(radians(i))), 1)

# Function to draw a face (smiley or frowny)
def draw_face(oled, smile=True):
    eye_y = 30
    mouth_y = 40
    mouth_radius = 10
    if not smile:
        mouth_y = 50
    
    draw_circle(oled, 56, eye_y, 2)   # Left eye
    draw_circle(oled, 72, eye_y, 2)   # Right eye
    draw_half_circle(oled, 64, mouth_y, mouth_radius, "up" if smile else "down")  # Smile or Frown
    draw_circle(oled, 64, 40, 20)  # Circle around the face
    oled.show()  # Update display
    
    
while True:
    try:
        # Read sensor data
        temp_str = str(bme.temperature)
        temp_str = temp_str[:-1]  # Remove the last character ('C')
        tempC = float(temp_str)  # Convert to float
        
        # Convert temperature to Fahrenheit
        tempF = (tempC * 9/5) + 32
        
        # Read other sensor data
        hum = bme.humidity
        pres = bme.pressure
        
        # Display sensor readings on the first OLED display
        oled.fill(0)  # Clear OLED display
        oled.text("Temperature:", 0, 0)
        oled.text("{:.2f} F".format(tempF), 0, 10)
        oled.text("Humidity:", 0, 20)
        oled.text(str(hum), 0, 30)
        oled.text("Pressure:", 0, 40)
        oled.text(str(pres) + " hPa", 0, 50)
        oled.show()  # Show the updated display
    
        # Read moisture level from sensor
        moisture_level = adc.read_u16()
        
        # Normalize moisture level to a percentage (0 to 100)
        moisture_percentage = 100 - ((moisture_level - MIN_MOISTURE_READING) / (MAX_MOISTURE_READING - MIN_MOISTURE_READING)) * 100
        moisture_percentage = min(100, max(0, moisture_percentage))  # Ensure the value is within [0, 100]
        
        # Display moisture level at the top of the second OLED display
        second_oled.fill(0)  # Clear OLED display
        second_oled.text("Moisture:", 0, 0)
        second_oled.text("{:.2f}%".format(moisture_percentage), 80, 0)
        
        # Determine facial expression based on moisture level
        if moisture_percentage > 40:
            draw_face(second_oled, smile=True)
        else:
            draw_face(second_oled, smile=False)
            
        # Prepare sensor data
        sensor_data = {
            "temperature": tempF,
            "humidity": hum,
            "pressure": pres,
            "moisture_percentage": moisture_percentage
        }
        
        # Convert sensor data to JSON
        sensor_json = json.dumps(sensor_data)
        
        # Send HTTP POST request to server
        response = urequests.post("http://yourwebsite.com/route", data=sensor_json, headers={'Content-Type': 'application/json'})
        response.close()
        
    except Exception as e:
        # Handle any exceptions during sensor reading
        print('An error occurred:', e)

    sleep(30)  # Sleep for 30 seconds before the next iteration

