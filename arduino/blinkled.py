from arduino import arduino
import time

# change COM5 to the serial port that Arduino IDE shows
board = arduino.Arduino('COM5')

# tell the board that we will use digital pin 2 as an output
board.output([2])

# digital pins are binary: they can only have two values: HIGH or LOW
# set pin 2 to high
board.setHigh(2)

# wait 3 seconds so that we can see the LED light up
time.sleep(3)

# set pin 2 to low
board.setLow(2)

# do it again
board.setHigh(2)
time.sleep(3)
board.setLow(2)

# release control of the board (end of the program)
board.close()
