from math import floor
from random import randint
from datetime import datetime

class Controller(object):
  def __init__(self, table, algorithm):
    self.records = table
    self.algorithm = algorithm

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
      j = randint(0, i)
      self.records[i], self.records[j] = self.records[j], self.records[i]

  def definesizes (self, sizes):
    if len(sizes) == 0:
      return -1
    if not sizes:
      return -1
    if len(sizes) > len(self.records):
      print "LEN SIZES,", len(sizes)
      return -1
    else:
      self.sizes = sizes
    return 0

  def splitdata (self):
    self.toss()
    chunks = []
    absolutesizes = [int(floor(len(self.records) * size)) for size in self.sizes]
    pivot = 0
    for size in absolutesizes:
      nextpivot = min(pivot + size, len(self.records))
      chunks.append(self.records[pivot:nextpivot])
      pivot = nextpivot
    return chunks

  def runalgorithm (self, n):
    while n >= 0:
      chunks = self.splitdata()
      teaching_set = chunks[0: len(chunks) - 1]
      classification_set = chunks[-1]
      t1 = datetime.now()
      res = self.algorithm.classify(teaching_set, classification_set)
      t2 = datetime.now()
      print "delta: %r" % (t2 - t1)
      n -= 1
