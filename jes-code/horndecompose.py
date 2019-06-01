import math
PI = 3.14159


def sinewave(amplitude, frequency, duration, sampPerSec):
  multiplier = frequency * (2 * PI)
  sine = makeEmptySoundBySeconds(3, int(sampPerSec))
  for s in range(0, getLength(sine)):
    value = amplitude*math.sin(float(s)/sampPerSec * multiplier)
    #print value
    setSampleValueAt(sine, s,value)
    
  return sine

def subTwoSounds(s1, s2):
  copy = duplicateSound(s2)
  for i in range(0, min(getLength(s1), getLength(s2))):
    newVal = (getSampleValueAt(s1, i) - getSampleValueAt(copy, i))
    setSampleValueAt(copy, i, newVal)
  
  return copy
    
s = makeSound("Ensoniq-SQ-1-French-Horn-C4.wav")
sampPerSec = getSamplingRate(s)
print(sampPerSec)

note1 = sinewave(1000, 261, 3, sampPerSec)
note2 = sinewave(1000, 261*2, 3, sampPerSec)
note3 = sinewave(500, 261*3, 3, sampPerSec)
note4 = sinewave(500, 261*4, 3, sampPerSec)
note5 = sinewave(500, 261*5, 3, sampPerSec)
note6 = sinewave(250, 261*6, 3, sampPerSec)



# we could also add them together into one sound
final = subTwoSounds(s, note1);
final = subTwoSounds(final, note2);
openSoundTool(final)
#final = addTwoSounds(note1, note2);
#final = addTwoSounds(final, note3);
#final = addTwoSounds(final, note4);
#final = addTwoSounds(final, note5);
#final = addTwoSounds(final, note6);



