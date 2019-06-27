const int trig = 9;
const int echo = 10;

float echoTimeInMicroseconds() {
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
  float duration_us = echoTimeInMicroseconds();
  // we use "s" to denote seconds
  float duration_s = duration_us * pow(10, -6);

  Serial.print("Total round trip time: ");
  Serial.print(duration_us);
  Serial.print(" us OR ");
  Serial.print(duration_s);
  Serial.println(" s");
  delay(100);
}
