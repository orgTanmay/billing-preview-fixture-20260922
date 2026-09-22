"""Whole-second durations with no clock or timezone dependency."""


def split_duration(seconds):
    """Return hours, minutes, and seconds; hours are not limited to a day."""
    if (
        isinstance(seconds, bool)
        or not isinstance(seconds, int)
        or seconds < 0
    ):
        raise ValueError("seconds must be a non-negative integer")
    hours, remainder = divmod(seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return hours, minutes, seconds
