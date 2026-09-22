"""Whitespace normalization for short display labels."""


def normalize_spaces(text):
    """Trim Unicode whitespace and join whitespace-separated words."""
    if not isinstance(text, str):
        raise ValueError("text must be a string")
    # Splitting without a separator also handles tabs and line breaks.
    words = text.split()
    return " ".join(words)
