"""Rounded means using only exact integer arithmetic."""


def rounded_mean(values):
    """Average a nonempty list or tuple of integers; ties go away from zero."""
    if not isinstance(values, (list, tuple)) or not values:
        raise ValueError("values must be a nonempty list or tuple")
    if any(isinstance(value, bool) or not isinstance(value, int) for value in values):
        raise ValueError("every value must be an integer")
    total = sum(values)
    quotient, remainder = divmod(abs(total), len(values))
    if remainder * 2 >= len(values):
        quotient += 1
    return -quotient if total < 0 else quotient
