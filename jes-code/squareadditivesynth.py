import math
PI = 3.14159

def sinewave(amplitude, frequency, duration):
  multiplier = frequency * (2 * PI)
  sine = makeEmptySoundBySeconds(3)
  sampPerSec = getSamplingRate(sine)
  for s in range(0, getLength(sine)):
    value = amplitude*math.sin(float(s)/sampPerSec * multiplier)
    #print value
    setSampleValueAt(sine, s,value)
    
  return sine

def addTwoSounds(s1, s2):
  copy = duplicateSound(s1)
  for i in range(0, getLength(copy)):
    newVal = (getSampleValueAt(copy, i) + getSampleValueAt(s2, i))
    setSampleValueAt(copy, i, newVal)
  
  return copy
    

# add odd partial harmonics
note1 = sinewave(1000, 261, 3)
note2 = sinewave(1000.0/3, 261*3, 3)
note3 = sinewave(1000.0/5, 261*5, 3)
note4 = sinewave(1000.0/7, 261*7, 3)



# we could also add them together into one sound

final = addTwoSounds(note1, note2);
final = addTwoSounds(final, note3);
final = addTwoSounds(final, note4);


openSoundTool(final)

