import unittest
from calculator import add
from prime import is_prime
from testexception import is_prime as p

class TestCalculator(unittest.TestCase):
    def test_add_positive_numbers(self):
        self.assertEqual(add(2, 3),5)
    def test_add_negative_numbers(self):
        self.assertEqual(add(-2, -3), -5)
    def test_add_positive_negative_numbers(self):
        self.assertEqual(add(2, -3), -1)
    def test_notprime_number(self):
        self.assertFalse(is_prime(4))
    def test_prime_number(self):
        self.assertTrue(is_prime(3)) 
    def test_exception(self):
        self.assertRaises(TypeError,p,6.4)  
    def test_exception(self):
        with self.assertRaises(TypeError):
            p(7)

if __name__ == "__main__":
    unittest.main()