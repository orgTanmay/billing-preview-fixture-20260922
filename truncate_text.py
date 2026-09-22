"""Bounded text labels measured in Unicode code points."""


def truncate_text(text, max_length, marker="…"):
    """Fit text and an optional truncation marker within max_length."""
    if not isinstance(text, str) or not isinstance(marker, str):
        raise ValueError("text and marker must be strings")
    if isinstance(max_length, bool) or not isinstance(max_length, int):
        raise ValueError("max_length must be an integer")
    if max_length < 0 or len(marker) > max_length:
        raise ValueError("max_length must be non-negative and fit the marker")
    if len(text) <= max_length:
        return text
    retained = max_length - len(marker)
    return text[:retained] + marker
