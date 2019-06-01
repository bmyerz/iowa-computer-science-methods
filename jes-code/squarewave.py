import math

def makeSquare(amplitude, duration, frequency, rate):
  s = makeEmptySoundBySeconds(duration, rate)
  for i in range( getLength(s) ):
    v = None
    if ( math.sin(2*pi*i*frequency/rate) > 0 ):
      v = 1
    else:
      v = -1
    
    setSampleValueAt(s, i, amplitude * v)
  
  return s

s = makeSquare(1000, 2, 400, 22000)
blockingPlay(s)
explore(s)