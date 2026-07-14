_cache = {}


def fibonacci(n):

    """
    Before: O(2ⁿ) time — each call branches into two recursive calls,
    recomputing the same values exponentially many times.
    fibonacci(5) computes fibonacci(3) twice, fibonacci(2) three times, etc.

    After: O(n) time, O(n) space — each value is computed exactly once and
    stored. Subsequent calls for the same n return from the cache in O(1).
    """

    if n in _cache:
        return _cache[n]

    if n <= 1:
        return n

    result = fibonacci(n - 1) + fibonacci(n - 2)
    _cache[n] = result
    return result
