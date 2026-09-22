"""Zero-padded decimal integers with an explicit sign convention."""


def pad_integer(number, digits):
    """Pad the magnitude to at least digits places, excluding a minus sign."""
    if isinstance(number, bool) or not isinstance(number, int):
        raise ValueError("number must be an integer")
    if isinstance(digits, bool) or not isinstance(digits, int) or digits < 0:
        raise ValueError("digits must be a non-negative integer")
    magnitude = str(abs(number)).zfill(digits)
    return "-" + magnitude if number < 0 else magnitude
