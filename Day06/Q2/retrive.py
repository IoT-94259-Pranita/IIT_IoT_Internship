import mysql.connector

connection = mysql.connector.connect(
    host="127.0.0.1",
    port = 3306,
    user = "root",
    password = "root",
    database = "smart_agriculture",
    use_pure = True
)

query = "select * from soil_moisture_readings";

cursor = connection.cursor()

cursor.execute(query)

soil_moisture_readings = cursor.fetchall()

for soil_moisture_reading in soil_moisture_readings:
 print(soil_moisture_reading)
    
cursor.close()

connection.close()