"""Integer-only percentage arithmetic for the synthetic fixture."""


def calculate_fee(amount_cents, rate_basis_points):
    """Round a non-negative basis-point fee to the nearest cent, half up."""
    for value in (amount_cents, rate_basis_points):
        if isinstance(value, bool) or not isinstance(value, int) or value < 0:
            raise ValueError("amount and rate must be non-negative integers")
    return (amount_cents * rate_basis_points + 5000) // 10000
