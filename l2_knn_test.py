# from http://www.jiaaro.com/KNN-for-humans/

import unittest
from l2_knn import KNN

class TestKNNClass(unittest.TestCase):
  def testFromKNNForHumans (self):
    training_set = [
      [
        [303, 3],
        [298, 3],
        [277, 3],
        [299, 3],
        [303, 4],
        [309, 3],
        [311, 3],
        [302, 3],
        [305, 3],
      ],
      [
        [370, 1],
        [377, 4],
        [382, 1],
        [374, 4],
        [359, 1],
        [366, 1],
        [373, 4],
        [371, 3]
      ],
      [
        [200, 10],
        [201, 11]
      ]
    ]
    classification_set = [
      [373, 1]
    ]
    k = 3
    knn = KNN(training_set, classification_set, k)
    clazzes = knn.classify()
    self.assertEqual(len(clazzes), 1)
    self.assertEqual(clazzes[0], 1)

suite = unittest.TestLoader().loadTestsFromTestCase(TestKNNClass)
unittest.TextTestRunner(verbosity=2).run(suite)