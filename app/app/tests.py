""""
Sample tests
"""
from django.test import SimpleTestCase

from app.calc import add

class CalcTests(SimpleTestCase):
    """Test the calc module"""
    def test_add_numbers(self):
        """Test the addition of two numbers"""
        res = add(5, 6)
        self.assertEqual(res, 11)

    # Adding two positive integers
    def test_adding_two_positive_integers(self):
        result = add(3, 5)
        self.assertEqual(result, 8)

    def test_adding_very_large_integers(self):
        result = add(10 ** 18, 10 ** 18)
        self.assertEqual(result, 2 * 10 ** 18)

    def test_add_negative_integers(self):
        result = add(-5, -3)
        self.assertEqual(result, -8)

    def test_add_positive_and_negative_integers(self):
        result = add(8, -3)
        self.assertEqual(result, 5)
