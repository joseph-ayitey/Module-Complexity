from typing import List, TypeVar

Number = TypeVar("Number", int, float)


def has_pair_with_sum(numbers: List[Number], target_sum: Number) -> bool:
    """
    Find if there is a pair of numbers that sum to a target value.

    Time Complexity: O(n²) — for each of n elements we check up to n-1 remaining
        elements, examining every possible pair
    Space Complexity: O(1) — no extra data structures, just index variables
    Optimal time complexity: O(n) — one pass: for each number check if its
        complement (target - number) has already been seen

    Refactor: walk the array once. For each number x, if (target_sum - x) is
    already in the seen set, a valid pair exists. Otherwise record x and move on.
    Trades O(1) space for O(n) space, but cuts time from O(n²) to O(n).
    """
    
    seen: set = set()
    for num in numbers:
        if target_sum - num in seen:
            return True 
        
        seen.add(num)
    return False
