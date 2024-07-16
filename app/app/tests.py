"""
Sample Tests
"""

from django.test import SimpleTestCase

from app import calc


class CalcTEsts(SimpleTestCase):
    """Test the calc module"""


    def test_add_numbers(self):
        
        res = calc.add(5,6)

        self.assertEqual(res, 11)



    def test_subtract_numbers(self):

        res = calc.subtract(20, 15)

        self.assertEqual(res, 5)

        
    