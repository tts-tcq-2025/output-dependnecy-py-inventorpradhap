def size(cms):
    """Determine the size based on the given measurement in centimeters.

    Args:
        cms (int or float): The measurement in centimeters.

    Returns:
        str: 'S' for small, 'M' for medium, 'L' for large.
    """
    if cms < 38:
        return 'S'
    elif cms < 42:
        return 'M'
    else:
        return 'L'


# Example assertions for testing
assert(size(37) == 'S')
assert(size(38) == 'M')
assert(size(40) == 'M')
assert(size(42) == 'L')
assert(size(43) == 'L')
print("All is well (maybe!)")
