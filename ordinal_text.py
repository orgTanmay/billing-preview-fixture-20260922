"""English ordinal labels for positive whole numbers."""


def format_ordinal(number):
    """Format a positive integer with its English ordinal suffix."""
    if isinstance(number, bool) or not isinstance(number, int) or number <= 0:
        raise ValueError("number must be a positive integer")
    if 11 <= number % 100 <= 13:
        suffix = "th"
    else:
        suffix = {1: "st", 2: "nd", 3: "rd"}.get(number % 10, "th")
    return f"{number}{suffix}"
