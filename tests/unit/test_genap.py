# from src.genap import genap
# def test_genap_salah():
#     assert not genap(5)

# def test_genap_benar():
#     assert genap(8)
 
import unittest
from src.genap import genap 

def is_even(number):
    return number % 2 == 0

def is_odd(number):
    return number % 2 != 0

class TestEvenOddFunctions(unittest.TestCase):

    def test_is_even(self):
        self.assertTrue(is_even(2))
        self.assertTrue(is_even(0))
        self.assertFalse(is_even(1))
        self.assertFalse(is_even(7))
        self.assertFalse(is_even(-3))

    def test_is_odd(self):
        self.assertTrue(is_odd(1))
        self.assertTrue(is_odd(7))
        self.assertFalse(is_odd(2))
        self.assertFalse(is_odd(0))
        self.assertFalse(is_odd(-4))

