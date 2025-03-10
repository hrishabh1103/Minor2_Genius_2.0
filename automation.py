import paho.mqtt.client as mqtt

BROKER = "broker.hivemq.com"  # Use your MQTT broker
PORT = 8883
client = mqtt.Client()

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT Broker!")
    else:
        print("Failed to connect")

client.on_connect = on_connect
client.connect(BROKER, PORT, 60)

def control_device(device, action):
    topic = f"home/{device}"
    client.publish(topic, action)
    print(f"Sent {action} command to {device}")

# Example Usage
control_device("lights", "on")
control_device("ac", "off")
control_device("fan", "on")
control_device("tv", "off") 