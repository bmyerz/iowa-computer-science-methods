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
    
note1 = sinewave(1000, 400, 3)
note2 = sinewave(1000, 500, 3)

# one way to play a harmony is play two separate sounds
play(note1)
blockingPlay(note2)

# we could also add them together into one sound
harmonyOf1And2 = addTwoSounds(note1, note2)
blockingPlay(harmonyOf1And2)
openSoundTool(harmonyOf1And2)
