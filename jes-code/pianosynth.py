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
    
note1 = sinewave(1000, 261, 3)
note1b = sinewave(125, 180, 3)
note1a = sinewave(125, 220, 3)
note1bb = sinewave(75, 160, 3)
note1aa = sinewave(75, 240, 3)

note2 = sinewave(1000, 261*2, 3)
note3 = sinewave(500, 261*3, 3)
note4 = sinewave(500, 261*4, 3)
note5 = sinewave(500, 261*5, 3)
note6 = sinewave(250, 261*6, 3)



# we could also add them together into one sound
final = addTwoSounds(note1, note1a);
final0 = addTwoSounds(final, note1b);
final0 = addTwoSounds(final0, note1bb);
final0 = addTwoSounds(final0, note1aa);

final = addTwoSounds(note1, note2);
final = addTwoSounds(final, note3);
final = addTwoSounds(final, note4);
final = addTwoSounds(final, note5);
final = addTwoSounds(final, note6);


openSoundTool(final)
openSoundTool(note1)
