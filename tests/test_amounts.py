import unittest
from decimal import Decimal

from amounts import apply_discount, split_evenly, subtotal
from basis_points import calculate_fee
from bounded_values import clamp
from ceiling_ratio import containers_needed
from money_format import format_cents


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

    def test_discount_large_integer(self):
        self.assertEqual(apply_discount(10**40 + 1, 50), 5 * 10**39 + 1)

    def test_discount_rejects_invalid_percent(self):
        with self.assertRaises(ValueError):
            apply_discount(100, 101)

    def test_basis_point_fee(self):
        self.assertEqual(calculate_fee(100, 150), 2)
        self.assertEqual(calculate_fee(100, 0), 0)

    def test_container_count(self):
        self.assertEqual(containers_needed(10, 3), 4)
        self.assertEqual(containers_needed(0, 3), 0)

    def test_money_text(self):
        self.assertEqual(format_cents(-5), "-0.05")
        self.assertEqual(format_cents(1200), "12.00")

    def test_bounds(self):
        self.assertEqual(clamp(-1, 0, 5), 0)
        self.assertEqual(clamp(8, 0, 5), 5)
