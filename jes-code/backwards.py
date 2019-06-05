s = makeSound("houstonproblem.wav")

backwards = duplicateSound(s)
for i in range(getLength(s)):
  v = getSampleValueAt(s, i)
  setSampleValueAt(backwards, getLength(s)-1-i, v)

blockingPlay(s)
blockingPlay(backwards)
