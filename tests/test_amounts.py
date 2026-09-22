import unittest
from decimal import Decimal

from amounts import apply_discount, split_evenly, subtotal
from basis_points import calculate_fee
from bounded_values import clamp
from ceiling_ratio import containers_needed
from money_format import format_cents
from digit_totals import digit_sum
from duration_parts import split_duration
from integer_mean import rounded_mean
from ordinal_text import format_ordinal
from padded_integer import pad_integer
from palindrome_text import is_palindrome
from prefix_text import remove_prefix
from ratio_parts import reduce_ratio
from round_to_step import round_to_step
from sequence_ranges import inclusive_count
from space_text import normalize_spaces
from truncate_text import truncate_text


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


class HelperTests(unittest.TestCase):
    def test_round_to_step(self):
        for value, step, expected in [(12, 5, 10), (15, 10, 20), (-15, 10, -20), (0, 7, 0)]:
            with self.subTest(value=value, step=step):
                self.assertEqual(round_to_step(value, step), expected)
        self.assertEqual(round_to_step(10**40 + 5, 10), 10**40 + 10)

    def test_round_to_step_validation(self):
        for args in [(True, 1), (1.5, 2), (1, False), (1, 0), (1, -2), (1, "2")]:
            with self.subTest(args=args), self.assertRaises(ValueError):
                round_to_step(*args)

    def test_ratio_reduction(self):
        self.assertEqual(reduce_ratio(12, 18), (2, 3))
        self.assertEqual(reduce_ratio(12, -18), (-2, 3))
        self.assertEqual(reduce_ratio(-12, -18), (2, 3))
        self.assertEqual(reduce_ratio(0, -18), (0, 1))
        self.assertEqual(reduce_ratio(10**40, 3 * 10**40), (1, 3))

    def test_ratio_validation(self):
        for args in [(1, 0), (True, 2), (1, False), (1.0, 2), (1, "2")]:
            with self.subTest(args=args), self.assertRaises(ValueError):
                reduce_ratio(*args)

    def test_digit_sum(self):
        self.assertEqual(digit_sum(-1203), 6)
        self.assertEqual(digit_sum(15, 2), 4)
        self.assertEqual(digit_sum(255, 16), 30)
        self.assertEqual(digit_sum(0), 0)

    def test_digit_sum_validation(self):
        for args in [(True, 10), (1.2, 10), (3, 1), (3, 0), (3, True), (3, "2")]:
            with self.subTest(args=args), self.assertRaises(ValueError):
                digit_sum(*args)

    def test_duration_parts(self):
        self.assertEqual(split_duration(3661), (1, 1, 1))
        self.assertEqual(split_duration(90000), (25, 0, 0))
        self.assertEqual(split_duration(0), (0, 0, 0))
        hours, minutes, seconds = split_duration(10**40)
        self.assertEqual(hours * 3600 + minutes * 60 + seconds, 10**40)

    def test_duration_validation(self):
        for value in [True, -1, 1.5, "60", None]:
            with self.subTest(value=value), self.assertRaises(ValueError):
                split_duration(value)

    def test_integer_mean(self):
        self.assertEqual(rounded_mean([1, 2]), 2)
        self.assertEqual(rounded_mean([-1, -2]), -2)
        self.assertEqual(rounded_mean((1, -1)), 0)
        self.assertEqual(rounded_mean([1, 1, 2]), 1)
        self.assertEqual(rounded_mean([10**40, 10**40 + 1]), 10**40 + 1)

    def test_integer_mean_validation(self):
        for values in [[], (), [True], [1, 2.5], ["1"], "12", None]:
            with self.subTest(values=values), self.assertRaises(ValueError):
                rounded_mean(values)

    def test_inclusive_count(self):
        self.assertEqual(inclusive_count(1, 6, 2), 3)
        self.assertEqual(inclusive_count(6, 1, -2), 3)
        self.assertEqual(inclusive_count(2, 2, -1), 1)
        self.assertEqual(inclusive_count(6, 1, 2), 0)
        self.assertEqual(inclusive_count(1, 6, -2), 0)
        self.assertEqual(inclusive_count(0, 10**40), 10**40 + 1)

    def test_inclusive_count_validation(self):
        for args in [(0, 1, 0), (True, 1, 1), (0, False, 1), (0, 1, True), (0, 1.5, 1)]:
            with self.subTest(args=args), self.assertRaises(ValueError):
                inclusive_count(*args)

    def test_ordinals(self):
        for number, expected in [(1, "1st"), (2, "2nd"), (3, "3rd"), (11, "11th"),
                                 (12, "12th"), (13, "13th"), (21, "21st"), (112, "112th")]:
            with self.subTest(number=number):
                self.assertEqual(format_ordinal(number), expected)

    def test_ordinal_validation(self):
        for value in [True, 0, -1, 1.0, "1", None]:
            with self.subTest(value=value), self.assertRaises(ValueError):
                format_ordinal(value)

    def test_space_normalization(self):
        self.assertEqual(normalize_spaces("  hello\tworld\nagain  "), "hello world again")
        self.assertEqual(normalize_spaces("a\u2003b"), "a b")
        self.assertEqual(normalize_spaces(" \t\n"), "")
        self.assertEqual(normalize_spaces(""), "")

    def test_space_validation(self):
        for value in [None, 12, b"text", ["text"]]:
            with self.subTest(value=value), self.assertRaises(ValueError):
                normalize_spaces(value)

    def test_prefix_removal(self):
        self.assertEqual(remove_prefix("pre-prefix", "pre-"), "prefix")
        self.assertEqual(remove_prefix("pre-pre-text", "pre-"), "pre-text")
        self.assertEqual(remove_prefix("text", ""), "text")
        self.assertEqual(remove_prefix("Text", "text"), "Text")
        self.assertEqual(remove_prefix("", "pre-"), "")

    def test_prefix_validation(self):
        for args in [(None, "a"), ("text", 1), (b"text", "t")]:
            with self.subTest(args=args), self.assertRaises(ValueError):
                remove_prefix(*args)

    def test_truncation(self):
        self.assertEqual(truncate_text("abcdef", 4), "abc…")
        self.assertEqual(truncate_text("abcdef", 3, "..."), "...")
        self.assertEqual(truncate_text("abc", 3), "abc")
        self.assertEqual(truncate_text("abc", 0, ""), "")
        self.assertEqual(truncate_text("éclair", 3, ""), "écl")

    def test_truncation_validation(self):
        for args in [(None, 3, ""), ("abc", True, ""), ("abc", -1, ""),
                     ("abc", 2.0, ""), ("abc", 2, "..."), ("abc", 3, None)]:
            with self.subTest(args=args), self.assertRaises(ValueError):
                truncate_text(*args)

    def test_palindromes(self):
        self.assertTrue(is_palindrome("A man, a plan, a canal: Panama!"))
        self.assertTrue(is_palindrome("12321"))
        self.assertTrue(is_palindrome("ßs"))
        self.assertTrue(is_palindrome("!!!"))
        self.assertFalse(is_palindrome("hello"))

    def test_palindrome_validation(self):
        for value in [None, 121, b"aba", ["aba"]]:
            with self.subTest(value=value), self.assertRaises(ValueError):
                is_palindrome(value)

    def test_integer_padding(self):
        self.assertEqual(pad_integer(-7, 3), "-007")
        self.assertEqual(pad_integer(7, 3), "007")
        self.assertEqual(pad_integer(1234, 2), "1234")
        self.assertEqual(pad_integer(0, 0), "0")

    def test_padding_validation(self):
        for args in [(True, 2), (1.5, 2), (1, False), (1, -1), (1, 1.5), (1, "2")]:
            with self.subTest(args=args), self.assertRaises(ValueError):
                pad_integer(*args)
