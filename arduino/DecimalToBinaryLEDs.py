from arduino import arduino
import time

b = arduino.Arduino('COM5')

digits = [False, False, False, False]
pins = [2, 3, 4, 5]

b.output(pins)

def setNumber(x):
    if (x < 0 or x > 15):
        return
    else:
        for i in range(0, 4):
            digits[i] = False
    
    print("Converting {}".format(x))
    
    i = 8
    logi = 3
    while (i > 0):
        if (x - i >= 0):
            print("   {}'s place is ON".format(i))
            digits[logi] = True
            x -= i;
        else:
            print("   {}'s place is OFF".format(i))
        
        # integer division
        i //= 2
        logi -= 1

def setPins():
    for i in range(0, 4):
        if digits[i]:
            b.setHigh(pins[i])
        else:
            b.setLow(pins[i])

for x in range(0, 15 + 1):
    setNumber(x)
    setPins()
    time.sleep(1)

b.close()
