# IoT Plant Monitoring System

This repository contains code for an IoT plant monitoring system using MicroPython and various sensors. The system collects temperature, humidity, pressure, and moisture level data from sensors and displays it on OLED screens. Additionally, it sends this data to a server for further analysis or monitoring.

## Hardware Components Used

- Raspberry Pi Pico W microcontroller
- BME280 4pin 3.3v sensor for temperature, humidity, and pressure
- [Moisture sensor](https://www.temu.com/1-5-10pcs-moisture-sensor-soil-moisture-sensor-hygrometer-for-arduino-soil-moisture-g-601099535775713.html?_oak_mp_inf=EOHvt6Km1ogBGiAxZGJlNDA0ODRmNDU0OWUxYjZiMWE0YTFkZmU1MGI0ZiC3r8D%2F9TE%3D&top_gallery_url=https%3A%2F%2Fimg.kwcdn.com%2Fproduct%2Fopen%2F2023-11-28%2F1701180298512-e026d3d0b322403f937ac4d80218cac8-goods.jpeg&spec_gallery_id=2065232334&refer_page_sn=10009&refer_source=0&freesia_scene=2&_oak_freesia_scene=2&_oak_rec_ext_1=MTI5&_oak_gallery_order=1448644806%2C294693496%2C1859282695%2C1223663875%2C1894223390&search_key=moisture%20sensor&refer_page_el_sn=200049&_x_sessn_id=vwesf7snyw&refer_page_name=search_result&refer_page_id=10009_1715301518738_wptxksg2vv)
- [SSD1306 OLED displays (two displays used in this project)](https://www.temu.com/0-96-inch-oled-display-module-128x64-12864-lcd-screen-board-for-arduino-oled--4pin-while-blue-yellow-oled-display-g-601099519017968.html?_oak_mp_inf=EPCHuZqm1ogBGiA4OWJkMzNmY2I4MWU0MjNkYmQzMzJmZTRmYzM3YTRkMyDxprv%2F9TE%3D&top_gallery_url=https%3A%2F%2Fimg.kwcdn.com%2Fproduct%2FFancyalgo%2FVirtualModelMatting%2F790a58b47ff2eae58df6d2644f72e10a.jpg&spec_gallery_id=2022200186&refer_page_sn=10009&refer_source=0&freesia_scene=2&_oak_freesia_scene=2&_oak_rec_ext_1=MjM5&_oak_gallery_order=847682794%2C1176108080%2C906997271%2C537107526%2C403756631&search_key=ssd%20oled&refer_page_el_sn=200049&refer_page_name=search_result&refer_page_id=10009_1715301425940_7zpp4nyhf9&_x_sessn_id=vwesf7snyw)
- [1.2" x 1.2" PCB Board](https://www.amazon.com/dp/B0CBPRBRTT?psc=1&ref=ppx_yo2ov_dt_b_product_details)
- WiFi connection (if available, can be omitted if not needed)


## Setup Instructions

1. **Connect the hardware components**: Follow the wiring specified in the code.
2. **Flash MicroPython firmware**: Flash MicroPython firmware to your Raspberry Pi Pico microcontroller.
3. **Upload the Python scripts**: Upload the Python scripts (`main.py`) to the microcontroller.
4. **Modify the script**: If using WiFi, modify the script with your WiFi credentials (`WIFI_SSID` and `WIFI_PASSWORD`).
5. **Configure server endpoint**: Ensure that the server endpoint (`http://yourwebsite.com/route`) matches your server setup.
6. **Power on the device**: The device will automatically start collecting sensor data.

## Usage

Once the system is set up and running:

- **Display sensor data**: Sensor data (temperature, humidity, pressure, and moisture level) will be displayed on the OLED screens.
- **Moisture-based facial expression**: The moisture level will determine the facial expression displayed on one of the OLED screens (smiley or frowny face).
- **Data transmission**: Sensor data will be sent to the specified server endpoint via HTTP POST requests in JSON format.
- **Error handling**: The system will handle exceptions during sensor readings and continue operation.

## Notes

- **WiFi usage**: If you're not using WiFi, you can omit the WiFi connection part from the script.
- **Server endpoint**: Ensure that the server endpoint is accessible and configured to receive data in JSON format.
- **Adjustable sleep time**: Adjust the sleep time (`sleep(30)`) in the script to change the interval between sensor readings and data transmissions.

## Dependencies

- MicroPython firmware
- BME280 library
- ssd1306 library
- urequests library (for HTTP requests)

## Completed Project

![Image Description](3d_print.jpg)

## Wiring Diagram

![Image Description](wiring_diagram.png)

## 3D print files
- The original 3D print design by [Qrome](https://www.thingiverse.com/thing:3573903) served as the basis, modified to accommodate a small solder board and all the sensors.

- [Print File 1](case.stl)
- [Print File 1](back.stl)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- This project was inspired by the need for a simple and efficient plant monitoring system.
- Thanks to the contributors of the MicroPython, BME280, and ssd1306 libraries for their valuable work.
