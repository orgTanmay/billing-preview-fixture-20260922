"""Exact rounding to integer-sized steps."""


def round_to_step(value, step):
    """Round to the nearest positive step, with ties away from zero."""
    if isinstance(value, bool) or not isinstance(value, int):
        raise ValueError("value must be an integer")
    if isinstance(step, bool) or not isinstance(step, int) or step <= 0:
        raise ValueError("step must be a positive integer")
    quotient, remainder = divmod(abs(value), step)
    if remainder * 2 >= step:
        quotient += 1
    rounded = quotient * step
    return -rounded if value < 0 else rounded
