void setup() {
    // our outputs are pins 2 and 3
    pinMode(2, OUTPUT);
    pinMode(3, OUTPUT);
}

void loop() {
   
    // an arbitrary sequence of blinks of the two LEDs
    digitalWrite(2, HIGH);
    delay(1000);
    digitalWrite(2, LOW);
    digitalWrite(3, HIGH);
    delay(1000);
    digitalWrite(2, HIGH);
    delay(1000);
    digitalWrite(2, LOW);
    digitalWrite(3, LOW);


    delay(1000);
    // As with BlinkLED.ino, since this code is inside of loop(),
    // it will keep repeating forever, unlike the Python versions.

}


