from typing import List, Sequence, TypeVar

ItemType = TypeVar("ItemType")


def find_common_items(
    first_sequence: Sequence[ItemType], second_sequence: Sequence[ItemType]
) -> List[ItemType]:
    """
    Find common items between two arrays.

    Time Complexity: O(n × m) — outer loop visits n items in first_sequence;
        inner loop scans up to m items in second_sequence for each one;
        the `i not in common_items` check adds another O(k) per match
    Space Complexity: O(n) — common_items holds at most n elements
    Optimal time complexity: O(n + m) — convert second_sequence to a Set (O(m)),
        then each membership check is O(1) instead of O(m)

    Refactor: build a set from second_sequence once (O(m)), then iterate
    first_sequence once using O(1) set lookup. Uses a result set to deduplicate.
    Trades a small amount of extra space for linear time overall.
    """

    second_set = set(second_sequence)
    seen: set = set()

    common_items: List[ItemType] = []
    for item in first_sequence:
       if item in second_set and item not in seen:
          seen.add(item)
          common_items.append(item)
    return common_items
