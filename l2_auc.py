# http://cs.ru.nl/~tomh/onderwijs/dm/dm_files/roc_auc.pdf
class AUC(object):
  def __init__(self):
    self.datapointsClass1 = []
    self.datapointsClass2 = []

  def nextresult(self, vector, actualclass, predictedclass, score):
    if actualclass == 0:
      self.datapointsClass1.append(score)
    else:
      self.datapointsClass2.append(score)

  def output():
    sum0 = 0
    coefficient = 1.0 / len(self.datapointsClass1) / len(self.datapointsClass2)
    for i in range(len(datapointsClass2)):
      for j in range(len(datapointsClass1)):
        if  datapointsClass2[i] > datapointsClass1[j]:
          sum0 += 1


    return sum0
