from typing import Dict, List


def calculate_sum_and_product(input_numbers: List[int]) -> Dict[str, int]:
    """
    Calculate the sum and product of integers in a list.

    Note: the sum is every number added together
    and the product is every number multiplied together
    so for example: [2, 3, 5] would return
    {
        "sum": 10, // 2 + 3 + 5
        "product": 30 // 2 * 3 * 5
    }
     Time Complexity: O(n) — two sequential loops, each visiting n elements once (O(2n) = O(n))
    Space Complexity: O(1) — only two accumulator variables, regardless of input size
    Optimal time complexity: O(n) — every element must be visited at least once; can't do better

    Refactor: collapsed two loops into one. Big O doesn't change (still O(n)), but the
    constant factor halves — we visit each element once instead of twice.
    """
    # Edge case: empty list
    if not input_numbers:
        return {"sum": 0, "product": 1}
    
    total = 0

    product = 1
    for current_number in input_numbers:
        total += current_number
        product *= current_number

    return {"sum": total, "product": product}
