# MQTT-Based Light Control

This project allows a user to control a simulated IoT light using MQTT.

## How It Works
1. The web interface (index.html) sends "ON" or "OFF" commands via MQTT.
2. The Python script (light_simulation.py) subscribes to the same MQTT topic and prints the light status.

## How to Run
1. Open `index.html` in a browser.
2. Run `light_simulation.py` using Python.
3. Click "Turn ON" or "Turn OFF" and check the Python script output.

## Dependencies
- MQTT.js (included via CDN)
- Python `paho-mqtt` (`pip install paho-mqtt`)
