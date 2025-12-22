import paho.mqtt.client as mqtt
import time

def on_publish(client, userdata, mid, reason_code, properties):
    appliance = input("Enter appliance name (Light/Fan/AC): ")
    status = input("Enter status (ON/OFF): ")

    message = f"{appliance},{status}"
    client.publish("home/control", message)

    print(f"Command sent → {message}")


publisher = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

publisher.on_publish = on_publish

publisher.connect("localhost")

publisher.loop_start()

publisher.publish("Light/Fan/AC", "ON")
publisher.publish("Light/Fan/AC", "OFF")

time.sleep(1)

publisher.loop_stop()
publisher.disconnect()