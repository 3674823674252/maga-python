import sys

class ConfusionMatrix(object):
  def __init__(self):
    self.hash = {}

  def nextresult(self, vector, actualclass, predictedclass):
    if not (actualclass in self.hash):
      self.hash[actualclass] = {}
    if not (predictedclass in self.hash[actualclass]):
      self.hash[actualclass][predictedclass] = 0

    self.hash[actualclass][predictedclass] += 1

  def output (self):
    predictedkeys = []
    for actualkey in self.hash.keys():
      for predictedkey in self.hash[actualkey].keys():
        if predictedkey in predictedkeys:
          pass
        else:
          predictedkeys.append(predictedkey)

    sys.stdout.write('\t\t')

    for key in predictedkeys:
      sys.stdout.write(key)
      sys.stdout.write('\t')

    sys.stdout.write('\n')

    for actualkey in self.hash.keys():
      sys.stdout.write(actualkey)
      sys.stdout.write('\t\t')
      for predictedkey in predictedkeys:
        if predictedkey in self.hash[actualkey]:
          sys.stdout.write(str(self.hash[actualkey][predictedkey]))
          sys.stdout.write('\t')
        else:
          sys.stdout.write('0\t')
      sys.stdout.write('\n')

  def testyourself (self):
    self.nextresult(0, 'a', 'b')
    self.nextresult(1, 'a', 'a')
    self.nextresult(2, 'b', 'a')
    self.nextresult(3, 'b', 'b')
    self.nextresult(4, 'b', 'a')
    self.output()