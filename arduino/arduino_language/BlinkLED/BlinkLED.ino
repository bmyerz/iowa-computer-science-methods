// All Arduino programs must define at least the following two functions: setup() and loop()

// the setup() function runs exactly once when the Arduino starts up
void setup() {
    // tell the board that we will use digital pin 2 as an output
    pinMode(2, OUTPUT); 
}

// the loop() function runs over and over again until you unplug or reprogram your Arduino!
void loop() {
    // digital pins are binary: they can only have two values: HIGH or LOW
    // set pin 2 to high
    digitalWrite(2, HIGH);

    // wait 3 seconds so that we can see the LED light up
    // the delay() function takes the amount of time *in milliseconds*
    delay(3000);

    // set pin 2 to low
    digitalWrite(2, LOW);

    // wait 3 seconds so that we can see the LED turn off
    delay(3000);

    // This BlinkLED.ino program is different from BlinkLED.py
    // in that it keeps blinking the LED forever instead of
    // just twice! See the comment above "void loop() {"
}



// This tutorial derived from
// https://www.arduino.cc/en/Tutorial/Blink
