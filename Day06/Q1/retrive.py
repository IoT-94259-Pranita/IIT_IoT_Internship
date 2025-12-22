import mysql.connector

connection = mysql.connector.connect(
    host="127.0.0.1",
    port = 3306,
    user = "root",
    password = "root",
    database = "iot_data",
    use_pure = True
)

query = "select * from sensor_readings";

cursor = connection.cursor()

cursor.execute(query)

sensor_readings = cursor.fetchall()

for sensor_reading in sensor_readings:
 print(sensor_reading)
    
cursor.close()

connection.close()