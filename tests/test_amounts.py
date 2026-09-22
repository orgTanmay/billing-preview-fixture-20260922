import unittest
from decimal import Decimal

from amounts import split_evenly, subtotal


class AmountTests(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(subtotal([]), Decimal("0.00"))

    def test_decimal_total(self):
        self.assertEqual(subtotal([("1.25", 3), ("0.10", 2)]), Decimal("3.95"))

    def test_invalid_quantity(self):
        with self.assertRaises(ValueError):
            subtotal([("1.25", -1)])

    def test_nonfinite_price(self):
        with self.assertRaises(ValueError):
            subtotal([("NaN", 1)])

    def test_exact_split(self):
        self.assertEqual(split_evenly(100, 3), [34, 33, 33])

    def test_invalid_people(self):
        with self.assertRaises(ValueError):
            split_evenly(100, 0)
