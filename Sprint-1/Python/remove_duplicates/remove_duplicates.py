from typing import List, Sequence, TypeVar

ItemType = TypeVar("ItemType")


def remove_duplicates(values: Sequence[ItemType]) -> List[ItemType]:
    """
    Remove duplicate values from a sequence, preserving the order of the first occurrence of each value.

 Time complexity: O(n²) — for each of n elements, the inner loop scans
        unique_items which grows up to n, making membership check O(n) each time
    Space complexity: O(n) — unique_items holds up to n elements
    Optimal time complexity: O(n) — use a Set for O(1) membership checks instead
        of scanning a list

    Refactor: a Set tracks what we've seen (O(1) lookup). We iterate once,
    appending only items not yet in the Set. Same O(n) space as before, but
    time drops from O(n²) to O(n).
    """
    seen: set = set()
    unique_items: List[ItemType]

    for value in values:
        if value in values:
            seen.add(value)
            unique_items.append(value)

    return unique_items
