import unittest
from BinarySearch import BinarySearch

class BinarySearch_test(unittest.TestCase):
  def test_not_found(self):
    self.assertEqual(BinarySearch(1,[]),-1)
    self.assertEqual(BinarySearch(1,[3]),-1)
    self.assertEqual(BinarySearch(7,[1,3,5]),-1)
    self.assertEqual(BinarySearch(2,[1,3,5]),-1)

  def test_item_in_first_position(self):
    self.assertEqual(BinarySearch(1,[1]),0)
    self.assertEqual(BinarySearch(1,[1,3,5]),0)
    self.assertEqual(BinarySearch(1,[1,3,5,7]),0)
    self.assertEqual(BinarySearch(1,[1,3,5,7,9]),0)

  def test_item_in_the_first_half(self):
    self.assertEqual(BinarySearch(3,[1,3,5,7,9]),1)
    self.assertEqual(BinarySearch(3,[1,3,5,7,9,11,13]),1)
    self.assertEqual(BinarySearch(5,[1,3,5,7,9,11,13]),2)
    self.assertEqual(BinarySearch(3,[1,3,5,7]),1)

  def test_item_is_in_the_middle(self):
    self.assertEqual(BinarySearch(3,[1,3,5]),1)
    self.assertEqual(BinarySearch(5,[1,3,5,7,9]),2)

  def test_item_is_in_the_second_half(self):
    self.assertEqual(BinarySearch(7,[1,3,5,7,9]),3)
    self.assertEqual(BinarySearch(7,[1,3,5,7]),3)
    self.assertEqual(BinarySearch(9,[1,3,5,7,9]),4)
