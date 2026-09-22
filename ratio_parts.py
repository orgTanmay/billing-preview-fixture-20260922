"""Canonical integer ratios without floating-point arithmetic."""

from math import gcd


def reduce_ratio(numerator, denominator):
    """Return coprime ratio parts with a strictly positive denominator."""
    for value in (numerator, denominator):
        if isinstance(value, bool) or not isinstance(value, int):
            raise ValueError("ratio parts must be integers")
    if denominator == 0:
        raise ValueError("denominator must be nonzero")
    divisor = gcd(numerator, denominator)
    if denominator < 0:
        divisor = -divisor
    return numerator // divisor, denominator // divisor
