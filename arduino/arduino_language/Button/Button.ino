
void setup() {
    // We are using digital pin 2 as an input from the outside world (the button!)
    pinMode(2, INPUT);

  // initialize serial communications at 9600 bits per second
  // Arduino IDE needs to have the
  // same setting of 9600
  // the particular value doesn't matter so much, rather it 
  // matters that this code and the IDE agree on it
  Serial.begin(9600);
}

// in Arduino language, we need to write the
// type of a new variable the first time it appears
// Here, the type int means t is an integer.
int t = 0;

// integers like t can only be given integer values
// so I couldn't do 
// int t = "Hello";
// or
// int t = 456.12


// print the state (True or False) of the button
// once per second
void loop() {
    // this is how we read digital pin 2
    // the value is True if the pin is receiving high voltage
    // and False if the pin is receiving low voltage
    int value = digitalRead(2);
    
    // use Serial.print to output a string... 
    Serial.print("At time ");
    Serial.print(t); // ... or a variable's value
    Serial.print(" the value is "); // (notice how we are including spaces in the string so it doesn't run together)
    Serial.print(value);
    // Use Serial.println (short for "print line") when you want to end the line (like pressing ENTER)
    Serial.println(); 
    
    // wait for 1 second
    delay(1000);
}


// This tutorial derived from 
// https://www.arduino.cc/en/Tutorial/Button
