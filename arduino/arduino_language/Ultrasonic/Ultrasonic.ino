const int trig = 9;
const int echo = 10;

float timeOfFlightMicroseconds() {
  // just make sure trig starts low
  digitalWrite(trig, LOW);
  delayMicroseconds(2);

  // HC-SR04 expects a 10us pulse on trig
  // to then initiate the ranging pulse
  digitalWrite(trig, HIGH);
  delayMicroseconds(10);
  digitalWrite(trig, LOW);

  // duration of the echo pulse
  // The echo output of HC-SR04 is high
  // from the time the trig pulse is finished
  // until the time the reflected sound is detected
  float duration = pulseIn(echo, HIGH);
  return duration;
}

void setup() {
  pinMode(trig, OUTPUT);
  pinMode(echo, INPUT);
  Serial.begin(9600);
}

void loop() {
  // we use "us" to denote microseconds (10^-6 seconds per microsecond)
  float duration_us = timeOfFlightMicroseconds();
  float duration_s = duration_us / 1000000;

  Serial.print("Total round trip time (us): ");
  Serial.print(duration_us);
  delay(100);
}
