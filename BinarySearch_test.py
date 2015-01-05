
import unittest
from BinarySearch import BinarySearch


class BinarySearch_test(unittest.TestCase):
  def test_not_found(self):
    self.assertEqual(BinarySearch(1,[]),-1)


