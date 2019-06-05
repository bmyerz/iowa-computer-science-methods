from arduino import arduino
import time

b = arduino.Arduino('COM5')

# Very important: even though this program does not
# write to any pins, you still need to call the output
# function with an empty list.
# By default, any pin that is not in the list of output
# pins is assumed to be an input pin.
b.output([])

# print the state (True or False) of the button
# once per second for 10 seconds
t = 0
while t < 10:
    # this is how we read digital pin 2
    # the value is True if the pin is receiving high voltage
    # and False if the pin is receiving low voltage
    value = b.getState(2)
    
    # you may or may not have seen Python's string format
    # function before. {0} is a placeholder for the first
    # argument (t) and {1} is a placeholder for the second argument (value)
    print("At time {0} values is {1}".format(t, value))
    
    time.sleep(1)
    t = t + 1

b.close()
