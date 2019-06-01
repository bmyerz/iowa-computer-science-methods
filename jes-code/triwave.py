def makeSaw(amplitude, duration, frequency, rate):
  s = makeEmptySoundBySeconds(duration, rate)
  for i in range( getLength(s) ):
    rising = i*float(frequency)/rate
    periodic = rising % 1
    setSampleValueAt(s, i, amplitude * periodic)
  
  return s

def makeTri(amplitude, duration, frequency, rate):
  s = makeSaw(amplitude, duration, frequency, rate)
  for i in range( getLength(s) ):
    trianglesAboveGround = abs(float(getSampleValueAt(s, i))/amplitude - 0.5)
    triangles = trianglesAboveGround * 4 - 1
    setSampleValueAt(s, i, amplitude * triangles)
  
  return s

def makeCubic(amplitude, duration, frequency, rate):
  s = makeEmptySoundBySeconds(duration, rate)
  for i in range( getLength(s) ):
    rising = i*float(frequency)/rate
    periodic = rising % 1
    cubic = periodic * periodic * periodic
    setSampleValueAt(s, i, amplitude * cubic)
  
  return s

def makeTicks(amplitude, duration, frequency, rate):
  s = makeEmptySoundBySeconds(duration, rate)
  for i in range( getLength(s) ):
    rising = i*float(frequency)/rate
    periodic = rising % 1
    if periodic <= 1.0 and periodic >= 0.95:
      periodic = 1
    else:
      periodic = 0 
    setSampleValueAt(s, i, amplitude * periodic)
  
  return s
  
  
s1 = makeSaw(1000, 2, 220, 22000)
s2 = makeTri(1000, 2, 220, 22000)
s3 = makeCubic(1000, 2, 220, 22000)
s4 = makeTicks(1000, 2, 220, 22000)
#blockingPlay(s1)
#blockingPlay(s2)
explore(s1)
explore(s2)
explore(s3)
explore(s4)