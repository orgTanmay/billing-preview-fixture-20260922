"""Literal, single-prefix string removal."""


def remove_prefix(text, prefix):
    """Remove one exact leading prefix; an empty prefix changes nothing."""
    if not isinstance(text, str) or not isinstance(prefix, str):
        raise ValueError("text and prefix must be strings")
    if prefix and text.startswith(prefix):
        return text[len(prefix):]
    return text
