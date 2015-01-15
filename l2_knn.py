# http://stackoverflow.com/a/1519293
def most_common(lst):
  mydict = {}
  cnt, itm = 0, ''
  for item in lst:
    mydict[item] = mydict.get(item, 0) + 1
    if mydict[item] >= cnt:
      cnt, itm = mydict[item], item

  return itm


def distance(item1, item2):
  sum_sq = 0

  for i in range(len(item1)):
    sum_sq = (item1[i] - item2[i]) ** 2

  sum_sq = sum_sq ** 0.5

  return sum_sq

def sort_by_distance(list, item):
  return sorted(list, key=lambda item0: distance(item, item0))


class KNN(object):
  def __init__(self, training_set, classification_set, k):
    self.training_set = training_set
    self.classification_set = classification_set
    self.k = k

  def classify(self):
    flattened_training_set = [item for sublist in self.training_set for item in sublist]
    clazzes = []
    for item in self.classification_set:
      flattened_training_set = sort_by_distance(flattened_training_set, item)
      top_k = flattened_training_set[:self.k]
      classes = []
      for top_k_item in top_k:
        for idx, chunk in enumerate(self.training_set):
          if top_k_item in chunk:
            classes.append(idx)
      clazz = most_common(classes)
      clazzes.append(clazz)

    return clazzes    

