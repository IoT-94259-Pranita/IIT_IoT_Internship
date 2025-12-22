# import mqtt module
import paho.mqtt.client as mqtt

def on_message(client, userdata, message):
    topic = message.topic
    value = float(message.payload.decode())

    if topic == "sensor/ldr":
       
        print(f"LDR Data Saved: {value}")

    elif topic == "sensor/lm35":
       
        print(f"Temperature Data Saved: {value} °C") 

# creat a client to  subscribe topic
subscriber = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

# add on_message into our subscriber
subscriber.on_message = on_message

# send connect message to publisher
subscriber.connect("localhost")

# subscribe for topic
subscriber.subscribe("sensor/ldr")
subscriber.subscribe("sensor/lm35")

# keep subscriber running continuously
subscriber.loop_forever()