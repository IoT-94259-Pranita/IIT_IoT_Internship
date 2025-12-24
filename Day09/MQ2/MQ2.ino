#define MQ2_PIN 34


void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  pinMode(MQ2_PIN,INPUT);
  Serial.println("MQ2 Sensor Warning up...");
}

void loop() {
  // put your main code here, to run repeatedly:
  int sensorValue=analogRead(MQ2_PIN);
  Serial.print("Gas level:");
  Serial.println(sensorValue);

  if(sensorValue>300)
  {
    Serial.println("Gas or Smoke Detected!!");
  }
  delay(1000); 
}
