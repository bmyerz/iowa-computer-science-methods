void setup() {
    // our outputs are pins 2 and 3
    pinMode(2, OUTPUT);
    pinMode(3, OUTPUT);
}

// this version acts more like TwoLEDs.py in that it blinks the LED pattern just once
// To achieve this, we want to keep track of whether we already ran the LED pattern.
// This is the perfect job for a bool variable (short for Boolean), which can either have
// the value true or false.
bool alreadyRan = false;

void loop() {
    if (alreadyRan) {
        // Goes here when alreadyRan is true
        // do Nothing! 
    } else {
        // Goes here when alreadyRan is false (i.e., just the first time loop() goes)

        alreadyRan = true; 

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
    }
}


