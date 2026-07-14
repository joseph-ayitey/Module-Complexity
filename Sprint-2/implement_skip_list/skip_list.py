import random


class _Node:
    def __init__(self, value, level):
        self.value = value
        self.forward = [None] * (level + 1)


class SkipList:

    """"
    A probabilistic sorted data structure with O(log n) average insert and
    contains, and O(n) to_list.

    Structure: multiple layers of linked lists. Layer 0 holds all elements in
    sorted order. Each higher layer is a sparse "express lane" — every node is
    independently promoted to the next layer with probability P=0.5. Starting
    a search from the top layer lets us skip large sections of the list before
    dropping down, giving O(log n) expected steps.

    Pre-computing angle: elements are kept sorted on insert (like a sorted
    linked list), and the express-lane indexes are maintained incrementally,
    so each subsequent contains check is fast without a full O(n) scan.
    """
    _MAX_LEVEL = 16
    _P = 0.5

    def __init__(self):
        self._level = 0
        self._head = _Node(None, self._MAX_LEVEL)

    def _random_level(self):
        level = 0
        while random.random() < self._P and level < self._MAX_LEVEL:
            level += 1
        return level

def insert(self, value):
    update = [None] * (self._MAX_LEVEL + 1)
    current = self._head

    for i in range(self._level, -1, -1):
        while current.forward[i] and current.forward[i].value < value:
            current = current.forward[i]
        update[i] = current

    # skip duplicates
    if current.forward[0] and current.forward[0].value == value:
        return

    new_level = self._random_level()
    if new_level > self._level:
        for i in range(self._level + 1, new_level + 1):
            update[i] = self._head
        self._level = new_level

    node = _Node(value, new_level)
    for i in range(new_level + 1):
        node.forward[i] = update[i].forward[i]
        update[i].forward[i] = node

    def __contains__(self, value):
        current = self._head
        for i in range(self._level, -1, -1):
            while current.forward[i] and current.forward[i].value < value:
                current = current.forward[i]
        current = current.forward[0]
        return current is not None and current.value == value


def to_list(self):
    result = []
    current = self._head.forward[0]
    while current:
        result.append(current.value)
        current = current.forward[0]
    return result