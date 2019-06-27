from arduino import arduino
import time

b = arduino.Arduino('COM5')

# make sure to call the output function on an empty
# list. This function call is still necessary even though
# we have no output pins in this example.
b.output([])

while (True):
    # read the voltage on pin A0
    # in general, use the number x for analog pin Ax
    v = b.analogRead(0)
    
    # print the voltage level
    print(v)
    
    # delay half a second
    time.sleep(0.5)


b.close()
