
void setup() {
  // initialize serial communications at 9600 bits per second
  // Arduino IDE needs to have the
  // same setting of 9600
  // the particular value doesn't matter so much, rather it 
  // matters that this code and the IDE agree on it
  Serial.begin(9600);


    // Note that we DO NOT need to 
    // set the pinMode for *anolog pins*
    // since they are already inputs
}

void loop() {
    // notice we didn't need "while True" as in Python
    // because loop() already repeats forever

    // read the voltage on pin A0
    int v = analogRead(A0);
    
    // use Serial.print to output a variable's value... 
    Serial.print(v);
    // Use Serial.println (short for "print line") when you want to end the line (like pressing ENTER)
    Serial.println(); 
    
    // delay half a second
    delay(500);
}

// This tutorial dervied from
// https://www.arduino.cc/en/Tutorial/AnalogInput
