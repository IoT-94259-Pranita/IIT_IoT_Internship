import paho.mqtt.client as mqtt
import sqlite3

def update_status(appliance, status):
    conn = sqlite3.connect("home_appliances.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO appliance_status (appliance, status) VALUES (?, ?)",
        (appliance, status)
    )

    conn.commit()
    conn.close()

def on_message(client, userdata, message):
   status = message.payload.decode()

   if message.topic == "Light/Fan/AC":
      print("Light turned", status)

   elif message.topic == "Light/Fan/AC":
       print("Fan turned", status)

subscriber = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)


subscriber.on_message = on_message

subscriber.connect("localhost")

subscriber.subscribe("Light/Fan/AC")

subscriber.loop_forever()