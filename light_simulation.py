import paho.mqtt.client as mqtt

print("🚀 MQTT Light Simulation Started... Waiting for messages...")

def on_connect(client, userdata, flags, reason_code, properties=None):
    print("Connected to MQTT Broker!")
    client.subscribe("/student_group/light_control")
    print("Subscribed to /student_group/light_control")

def on_message(client, userdata, msg, properties=None):
    message = msg.payload.decode()
    print(f"📥 Received message: {message}")  
    if message == "ON":
        print("💡 Light is TURNED ON")
    elif message == "OFF":
        print("💡 Light is TURNED OFF")

client = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION2)
client.on_connect = on_connect
client.on_message = on_message

client.connect("broker.hivemq.com", 1883, 60)

client.loop_forever()
