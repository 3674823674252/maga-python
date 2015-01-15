import os.path
from os import linesep
from sys import maxint

class CSVTable(object):
  def __init__(self, filename, headers):
    file = open(filename).readlines()
    if headers:
      self.headers = file[0:1][0].split(',')
      if self.headers:
        self.headers[-1] = self.headers[-1].replace('\n', '')
      self.records = file[1:]
    else:
      self.records = file[0:]
    if self.records:
      for idx, rec in enumerate(self.records):
        self.records[idx] = rec.split(',')
        self.records[idx][-1] = self.records[idx][-1].replace('\n', '')
        for idx0, field in enumerate(self.records[idx]):
          try:
            self.records[idx][idx0] = int(field)
          except ValueError:
            True

  def flush(self, dest):
    if not os.path.isfile(dest):
      print '%s is not a file, provide correct file' % dest
      return -1
    try:
      file = open(dest, 'w')
      if hasattr(self, 'headers'):
        file.write(','.join(self.headers) + linesep)
      recs = []
      for rec in self.records:
        recs.append(','.join(str(field) for field in rec))
      file.write(linesep.join(recs))
      return 0
    except IOError as e:
      print 'could not write to %s, i/o error %r' % (dest, e)
      return -1

  def sethead(self, head):
    self.headers = head

  def setahead(self, num, head):
    if not self.headers:
      return -1


    if num < len(self.headers) and num >= 0:
      self.headers[num] = head
    return 0

  def fillblanks(self, opt, val):
    if opt == 'const' and val:
      for rec in self.records:
        for idx, field in enumerate(rec):
          if field == '':
            rec[idx] = val

    if opt == 'midall':
      for rec in self.records:
        numset = 0
        accum = 0
        for idx, field in enumerate(rec):
          if isinstance(field, int):
            numset+= 1
            accum += field

        if numset == 0:
          continue

        mean = accum / numset

        for idx, field in enumerate(rec):
          if field == '':
            rec[idx] = mean

    if opt == 'midclass':
      lenrec = len(self.records[0])

      for clss in range(0, lenrec):
        numset = 0
        accum = 0

        for rec in self.records:
          if isinstance(rec[clss], int):
            numset+= 1
            accum += rec[clss]

        if numset == 0:
          continue

        mean = accum / numset

        for rec in self.records:
          if rec[clss] == '':
            rec[clss] = mean

  def normalize(self, opt):
    if opt == 'maxmin':
      for rec in self.records:
        max = -maxint
        min = maxint

        for idx, f in enumerate(rec):
          if not isinstance(f, int):
            continue
          if f > max:
            max = f
          if f < min:
            min = f

        if max == min:
          continue

        for idx, f in enumerate(rec):
          if isinstance(f, (float, int)):
            rec[idx] = ( float(f) - min) / (max - min)

    if opt == 'var':
      for rec in self.records:
        numset = 0
        accum = 0

        for idx, f in enumerate(rec):
          if not isinstance(f, (float, int)):
            continue
          numset+= 1
          accum += f

        if numset == 0:
          continue

        mean = accum / numset

        for idx, f in enumerate(rec):
          if not isinstance(f, (float, int)):
            continue

          rec[idx] = f - mean

  def stats(self):
    for rec in self.records:
      numset = 0
      accum = 0

      for idx, f in enumerate(rec):
        if not isinstance(f, (float, int)):
          continue
        numset+= 1
        accum += f

      if numset == 0:
        continue

      mean = accum / numset

      var = []

      for idx, f in enumerate(rec):
        if not isinstance(f, (float, int)):
          var.append(None)
        else:
          var.append(f - mean)

      reccopy = sorted(rec[:])

      q1 = 0
      q3 = 0
      idxq1 = 0
      idxq3 = 0

      if len(rec) % 2 != 0:
        idxq1 = int(int((len(rec) + 1) / 2) / 2) - 1
        idxq3 = int(int((len(rec) + 1) / 2 + 1 + len(rec)) / 2) - 1
      else:
        idxq1 = int(int(len(rec) / 2) / 2) - 1
        idxq3 = int(int(len(rec) / 2 + 1 + len(rec)) / 2) - 1

      q1 = rec[idxq1]
      q3 = rec[idxq3]

      print "For record %r" % rec
      print "Quantiles: %r %r %r" % (q1, mean, q3)
      print "Variances: %r" % var
      print "Fields set: %r" % numset