"""Inclusive integer sequence sizes without allocating the sequence."""


def inclusive_count(start, stop, step=1):
    """Count a stepped sequence including stop when the step reaches it."""
    for value in (start, stop, step):
        if isinstance(value, bool) or not isinstance(value, int):
            raise ValueError("start, stop, and step must be integers")
    if step == 0:
        raise ValueError("step must be nonzero")
    if step > 0:
        return 0 if start > stop else (stop - start) // step + 1
    return 0 if start < stop else (start - stop) // -step + 1
