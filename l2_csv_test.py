import unittest
from l2_csv import CSVTable

class TestCSVClass(unittest.TestCase):

  def testLoadFileWithoutHeaders (self):
    table = CSVTable('l2_csv_test_1.txt', 0)
    self.assertFalse(hasattr(table, 'headers'))

  def testLoadFileWithHeaders (self):
    table = CSVTable('l2_csv_test_1.txt', 1)
    self.assertTrue(hasattr(table, 'headers'))

  def testHeaderContent (self):
    table = CSVTable('l2_csv_test_1.txt', 1)
    self.assertEqual(table.headers[0], 'a')
    self.assertEqual(table.headers[1], 'b')
    self.assertEqual(table.headers[2], 'c')
    self.assertEqual(table.headers[3], 'd')

  def testRecordsContentWithoutHeaders (self):
    table = CSVTable('l2_csv_test_1.txt', 0)
    self.assertEqual(table.records[0][0], 'a')
    self.assertEqual(table.records[0][1], 'b')
    self.assertEqual(table.records[0][2], 'c')
    self.assertEqual(table.records[0][3], 'd')
    self.assertEqual(table.records[1][0], 0)
    self.assertEqual(table.records[1][1], 1)
    self.assertEqual(table.records[1][2], 2)
    self.assertEqual(table.records[1][3], 3)
    self.assertEqual(len(table.records), 2)

  def testRecordsContentWithHeaders (self):
    table = CSVTable('l2_csv_test_1.txt', 1)
    self.assertEqual(table.records[0][0], 0)
    self.assertEqual(table.records[0][1], 1)
    self.assertEqual(table.records[0][2], 2)
    self.assertEqual(table.records[0][3], 3)
    self.assertEqual(len(table.records), 1)

  def testFlushingToWrongFile (self):
    table = CSVTable('l2_csv_test_1.txt', 1)
    self.assertEqual(table.flush('wrong_file'), -1)

  def testFlushingToRightFileWithoutHeaders (self):
    table = CSVTable('l2_csv_test_1.txt', 0)
    self.assertEqual(table.flush('l2_csv_test_out.txt'), 0)
    file = open('l2_csv_test_out.txt').readlines()
    self.assertEqual(len(file), 2)
    self.assertEqual(file[0], 'a,b,c,d\n')
    self.assertEqual(file[1], '0,1,2,3')

  def testFlushingToRightFileWithHeaders (self):
    table = CSVTable('l2_csv_test_1.txt', 1)
    self.assertEqual(table.flush('l2_csv_test_out.txt'), 0)
    file = open('l2_csv_test_out.txt').readlines()
    self.assertEqual(len(file), 2)
    self.assertEqual(file[0], 'a,b,c,d\n')
    self.assertEqual(file[1], '0,1,2,3')

  def testSetHeadWithoutPrevHead (self):
    table = CSVTable('l2_csv_test_1.txt', 0)
    self.assertFalse(hasattr(table, 'headers'))
    table.sethead('test-head')
    self.assertTrue(hasattr(table, 'headers'))

  def testSetHeadWithPrevHead (self):
    table = CSVTable('l2_csv_test_1.txt', 1)
    self.assertTrue(hasattr(table, 'headers'))
    self.assertNotEqual(table.headers, 'test-head')
    table.sethead('test-head')
    self.assertTrue(hasattr(table, 'headers'))
    self.assertEqual(table.headers, 'test-head')

  def testSetAHeadWithoutHead (self):
    table = CSVTable('l2_csv_test_1.txt', 0)
    self.assertEqual(table.setahead(0, 'test-head'), -1)

  def testSetAHeadWithoutHead (self):
    table = CSVTable('l2_csv_test_1.txt', 1)
    self.assertEqual(table.setahead(0, 'test-head'), 0)
    self.assertEqual(table.headers[0], 'test-head')
    self.assertEqual(table.headers[1], 'b')
    self.assertEqual(table.headers[2], 'c')
    self.assertEqual(table.headers[3], 'd')

  def testFillBlanksWithConst (self):
    table = CSVTable('l2_csv_test_2.txt', 1)
    table.fillblanks('const', 100)
    self.assertEqual(table.records[0][0], 0)
    self.assertEqual(table.records[0][1], 1)
    self.assertEqual(table.records[0][2], 2)
    self.assertEqual(table.records[0][3], 3)
    self.assertEqual(table.records[1][0], 0)
    self.assertEqual(table.records[1][1], 100)
    self.assertEqual(table.records[1][2], 2)
    self.assertEqual(table.records[1][3], 6)
    self.assertEqual(table.records[2][0], 1)
    self.assertEqual(table.records[2][1], 1)
    self.assertEqual(table.records[2][2], 3)
    self.assertEqual(table.records[2][3], 4)

  def testFillBlanksWithMidall (self):
    table = CSVTable('l2_csv_test_2.txt', 1)
    table.fillblanks('midall', None)
    self.assertEqual(table.records[0][0], 0)
    self.assertEqual(table.records[0][1], 1)
    self.assertEqual(table.records[0][2], 2)
    self.assertEqual(table.records[0][3], 3)
    self.assertEqual(table.records[1][0], 0)
    self.assertEqual(table.records[1][1], 2)
    self.assertEqual(table.records[1][2], 2)
    self.assertEqual(table.records[1][3], 6)
    self.assertEqual(table.records[2][0], 1)
    self.assertEqual(table.records[2][1], 1)
    self.assertEqual(table.records[2][2], 3)
    self.assertEqual(table.records[2][3], 4)

suite = unittest.TestLoader().loadTestsFromTestCase(TestCSVClass)
unittest.TextTestRunner(verbosity=2).run(suite)
