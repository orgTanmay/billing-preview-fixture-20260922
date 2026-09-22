"""Pure helpers for a synthetic shopping-list example."""

from decimal import Decimal, ROUND_HALF_UP


def subtotal(items):
    """Return the sum of non-negative unit prices times quantities."""
    result = Decimal("0")
    for price, quantity in items:
        amount = Decimal(str(price))
        if not amount.is_finite() or amount < 0:
            raise ValueError("price must be finite and non-negative")
        if isinstance(quantity, bool) or not isinstance(quantity, int) or quantity < 0:
            raise ValueError("quantity must be a non-negative integer")
        result += amount * quantity
    return result.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)


def split_evenly(total_cents, people):
    """Split integer cents exactly; earlier recipients get remainder cents."""
    if isinstance(total_cents, bool) or not isinstance(total_cents, int) or total_cents < 0:
        raise ValueError("total must be a non-negative integer")
    if isinstance(people, bool) or not isinstance(people, int) or people <= 0:
        raise ValueError("people must be a positive integer")
    quotient, remainder = divmod(total_cents, people)
    return [quotient + (index < remainder) for index in range(people)]


def apply_discount(total_cents, percent):
    """Return integer cents after a whole-number percentage discount."""
    if isinstance(total_cents, bool) or not isinstance(total_cents, int) or total_cents < 0:
        raise ValueError("total must be a non-negative integer")
    if isinstance(percent, bool) or not isinstance(percent, int) or not 0 <= percent <= 100:
        raise ValueError("percent must be an integer between zero and one hundred")
    discounted_hundredths = total_cents * (100 - percent)
    return (discounted_hundredths + 50) // 100
