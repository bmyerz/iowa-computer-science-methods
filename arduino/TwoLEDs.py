from arduino import arduino
import time

b = arduino.Arduino('COM5')

# give both pins 2 and 3 in the list
b.output([2,3])

# an arbitrary sequence of blinks of the two LEDs
b.setHigh(2)
time.sleep(1)
b.setLow(2)
b.setHigh(3)
time.sleep(1)
b.setHigh(2)
time.sleep(1)
b.setLow(2)
b.setLow(3)


b.close()
