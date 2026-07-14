from typing import List

_cache = {}


def ways_to_make_change(total: int) -> int:
    """
    Given access to coins with the values 1, 2, 5, 10, 20, 50, 100, 200, returns a count of all of the ways to make the passed total value.

    For instance, there are two ways to make a value of 3: with 3x 1 coins, or with 1x 1 coin and 1x 2 coin.
    """
    return ways_to_make_change_helper(total, [200, 100, 50, 20, 10, 5, 2, 1])


def ways_to_make_change_helper(total: int, coins: List[int]) -> int:
    """
     Before: O(exponential) — many (total, coins) subproblems are recomputed
    repeatedly as the recursion branches into overlapping sub-trees.

    After: O(total × len(coins)) time and space — each unique (total, coins)
    pair is computed once and cached. Subsequent calls return in O(1).

    Cache key is (total, tuple(coins)) because the result depends on both the
    remaining total and which coins are still available.
    """
    key = (total, tuple(coins))
    if key in _cache:
        return _cache[key]
    

    if total == 0 or len(coins) == 0:
        return 0

    ways = 0
    for coin_index in range(len(coins)):
        coin = coins[coin_index]
        count_of_coin = 1
        while coin * count_of_coin <= total:
            total_from_coins = coin * count_of_coin
            if total_from_coins == total:
                ways += 1
            else:
                ways += ways_to_make_change_helper(
                    total - total_from_coins, coins=coins[coin_index + 1:]
                )
            count_of_coin += 1
            _cache[key] = ways
    return ways
