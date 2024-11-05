# dashboard/mqtt.py

import paho.mqtt.client as mqtt
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

def on_connect(client, userdata, flags, rc):
    client.subscribe("sensor/temperature")

def on_message(client, userdata, msg):
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        'temperature_data',
        {
            'type': 'send_temperature_data',
            'message': msg.payload.decode()
        }
    )

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("mqtt_broker_address", 1883, 60)  # Remplacez par votre adresse de broker
client.loop_start()
