import unittest
### from http://www.jiaaro.com/KNN-for-humans/

from l2_auc import AUC

class TestAUCClass(unittest.TestCase):
  def testRuns (self):
    auc = AUC()
    auc.nextresult('vector1', 0, 1, 100);

suite = unittest.TestLoader().loadTestsFromTestCase(TestAUCClass)
unittest.TextTestRunner(verbosity=2).run(suite)