"""Plain decimal text formatting without locale dependencies."""


def format_cents(cents):
    """Format an integer cent amount with exactly two decimal places."""
    if isinstance(cents, bool) or not isinstance(cents, int):
        raise ValueError("cents must be an integer")
    sign = "-" if cents < 0 else ""
    whole, remainder = divmod(abs(cents), 100)
    return f"{sign}{whole}.{remainder:02d}"
