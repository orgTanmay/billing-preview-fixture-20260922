"""Simple integer bounds for the synthetic test repository."""


def clamp(value, lower, upper):
    """Return value constrained to the inclusive integer bounds."""
    for number in (value, lower, upper):
        if isinstance(number, bool) or not isinstance(number, int):
            raise ValueError("value and bounds must be integers")
    if lower > upper:
        raise ValueError("lower bound must not exceed upper bound")
    return min(upper, max(lower, value))
