import unittest
from BinarySearch import BinarySearch

class BinarySearch_test(unittest.TestCase):
  def test_not_found(self):
    self.assertEqual(BinarySearch(1,[]),-1)
    self.assertEqual(BinarySearch(1,[3]),-1)

  def test_item_in_first_position(self):
    self.assertEqual(BinarySearch(1,[1]),0)


