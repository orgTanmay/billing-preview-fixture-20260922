import unittest
from decimal import Decimal

from amounts import apply_discount, split_evenly, subtotal


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

    def test_discount_rounding(self):
        self.assertEqual(apply_discount(101, 50), 51)

    def test_discount_full(self):
        self.assertEqual(apply_discount(101, 100), 0)

    def test_discount_rejects_invalid_percent(self):
        with self.assertRaises(ValueError):
            apply_discount(100, 101)
