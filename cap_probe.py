"""A tiny synthetic fixture for a preview review-admission check."""


def non_negative_difference(left, right):
    """Return the non-negative difference of two whole numbers."""
    for value in (left, right):
        if isinstance(value, bool) or not isinstance(value, int):
            raise ValueError("values must be integers")
    return max(0, left - right)
