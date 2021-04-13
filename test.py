import unittest
from random import randint

from main import RadixSort as sort

class TestStringMethods(unittest.TestCase):

  def test_empty(self):
      self.assertEqual(sort([]), [])

  def test_one_element_array(self):
      self.assertEqual(sort([1]), [1])

  def test_first(self):
      self.assertEqual(sort([12, 31, 3]), [3, 12, 31])

  def test_second(self):
      self.assertEqual(sort([0, 22, 0]), [0, 0, 22])

  def test_third(self):
      self.assertEqual(sort([442, 197, 5003, 109]), [109, 197, 442, 5003])

  def test_fourth(self):
      self.assertEqual(sort([1, 11, 1, 1]), [1, 1, 1, 11])

  def test_fifth(self):
      self.assertEqual(sort([235236, 54678348, 2348235, 124125]), [124125, 235236, 2348235, 54678348])

  def test_sixth(self):
      self.assertEqual(sort([301, 310, 700, 70, 37]), [37, 70, 301, 310, 700])

  def test_more_numbers(self):
    array = []
    for i in range(1000):
        array.append(randint(0, 10000))
    self.assertEqual(sort(array),
                    sorted(array))

if __name__ == '__main__':
    unittest.main()