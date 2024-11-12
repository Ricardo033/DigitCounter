import unittest
from decimal import Decimal
from fractions import Fraction
from function import count_integer_digits  # Replace 'your_script' with your actual script name

class TestCountIntegerDigits(unittest.TestCase):

    def test_positive_integers(self):
        self.assertEqual(count_integer_digits(100), 3)
        self.assertEqual(count_integer_digits(999), 3)
        self.assertEqual(count_integer_digits(5), 1)

    def test_negative_integers(self):
        self.assertEqual(count_integer_digits(-100), 3)
        self.assertEqual(count_integer_digits(-9), 1)

    def test_floats(self):
        self.assertEqual(count_integer_digits(3.1415), 1)
        self.assertEqual(count_integer_digits(-123.456), 3)

    def test_zero(self):
        self.assertEqual(count_integer_digits(0), 1)

    def test_large_numbers(self):
        self.assertEqual(count_integer_digits(10**5), 6)
        self.assertEqual(count_integer_digits(-10**10), 11)

    def test_fractions(self):
        self.assertEqual(count_integer_digits(Fraction(123, 10)), 2)  # 123/10 = 12.3 -> 12 has 2 digits
        self.assertEqual(count_integer_digits(Fraction(-456, 10)), 2)  # -456/10 = -45.6 -> 45 has 2 digits

    def test_decimals(self):
        self.assertEqual(count_integer_digits(Decimal("123.456")), 3)
        self.assertEqual(count_integer_digits(Decimal("-789.001")), 3)

    def test_complex_numbers(self):
        self.assertEqual(count_integer_digits(3 + 4j), 1)  # Only count the integer part of real component
        self.assertEqual(count_integer_digits(-99 + 100j), 2)  # Only count integer part of real component

    def test_invalid_string_input(self):
        self.assertEqual(count_integer_digits("hello"), "Invalid input 'hello'. Please provide a valid real number.")
        self.assertEqual(count_integer_digits("hi_1020"), "Invalid input 'hi_1020'. Please provide a valid real number.")

if __name__ == "__main__":
    unittest.main()