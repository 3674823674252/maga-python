from random import randint

class Controller(object):
  def __init__(self, table, algorithm, evaluator):
    self.records = records
    self.algorithm = algorithm
    self.evaluator = evaluator

    sizes = []
    percent = 1.0 / len(self.records)
    total = 0

    while total < 1.0:
      sizes.append(percent)
      total += percent

    self.definesizes(sizes)

  def toss (self):
    ## Knuth's tossing algorithm
    for i in reversed(range(len(self.records))):
      seed = randint(0, i)
      self.records[i], self.records[j] = self.records[j], self.records[i]

  def definesizes (self, sizes):
    if len(sizes) == 0:
      return -1
    if not sizes:
      return -1
    if len(sizes) >= len(self.records):
      return -1
    else:
      self.sizes = sizes
    return 0

  def splitdata (self):
    self.toss()
    chunks = []
    absolutesizes = floor(len(self.records) * size) for size in self.sizes
    pivot = 0
    for size in absolutesizes:
      nextpivot = min(pivot + size, len(self.records))
      chunks.append(self.records[pivot: nextpivot])
      pivot = nextpivot
    return chunks

  def runalgorithm (self):
    chunks = self.splitdata()
    