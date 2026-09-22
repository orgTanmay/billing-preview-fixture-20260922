"""Digit arithmetic for whole-number identifiers."""


def digit_sum(value, base=10):
    """Sum the digits of an integer's magnitude in a base of at least two."""
    if isinstance(value, bool) or not isinstance(value, int):
        raise ValueError("value must be an integer")
    if isinstance(base, bool) or not isinstance(base, int) or base < 2:
        raise ValueError("base must be an integer of at least two")
    remaining, total = abs(value), 0
    while remaining:
        remaining, digit = divmod(remaining, base)
        total += digit
    return total
