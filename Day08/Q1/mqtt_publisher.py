# import mqtt module
import paho.mqtt.client as mqtt
import random
import time

def on_publish(client, userdata, mid, reason_code, properties):
  
    ldr_value = random.randint(0, 1023)       
    temp_value = round(random.uniform(20, 35), 2)  

    client.publish("sensor/ldr", ldr_value)
    client.publish("sensor/lm35", temp_value)

    print(f"Published LDR: {ldr_value}")
    print(f"Published Temperature: {temp_value} °C")

    time.sleep(5)
   

# creat a client to publish data
publisher = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

# add on_publish into our publisher
publisher.on_publish = on_publish

# send connect message to publisher
publisher.connect("localhost")

# publish the message
publisher.publish("sensor/ldr", 2048)
publisher.publish("sensor/lm35", 2048)

# disconnect from broker
publisher.disconnect()