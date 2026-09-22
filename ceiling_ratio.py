"""Whole-unit packaging calculations for synthetic examples."""


def containers_needed(items, capacity):
    """Return the smallest container count that can hold all items."""
    if isinstance(items, bool) or not isinstance(items, int) or items < 0:
        raise ValueError("items must be a non-negative integer")
    if isinstance(capacity, bool) or not isinstance(capacity, int) or capacity <= 0:
        raise ValueError("capacity must be a positive integer")
    return (items + capacity - 1) // capacity
