# from http://www.jiaaro.com/KNN-for-humans/

import unittest
from l2_knn import KNN
from l2_controller import Controller

class TestControllClass(unittest.TestCase):
  def testRuns (self):
    data = [
        [303, 3],
        [298, 3],
        [277, 3],
        [299, 3],
        [303, 4],
        [309, 3],
        [311, 3],
        [302, 3],
        [305, 3],
        [370, 1],
        [377, 4],
        [382, 1],
        [374, 4],
        [359, 1],
        [366, 1],
        [373, 4],
        [371, 3],
        [200, 10],
        [201, 11],
        [373, 1]
    ]

    k = 3
    knn = KNN(k)
    controller = Controller(data, knn)
    controller.runalgorithm(5)

suite = unittest.TestLoader().loadTestsFromTestCase(TestControllClass)
unittest.TextTestRunner(verbosity=2).run(suite)