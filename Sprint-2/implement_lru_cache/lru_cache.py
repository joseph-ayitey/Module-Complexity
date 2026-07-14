class _Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value 
        self.prev = None
        self.next = None


class LruCache:
    """
    LRU cache backed by a dict + doubly linked list.

    dict:  key → Node          — O(1) lookup
    list:  head=most recent,
           tail=least recent   — O(1) move-to-front and evict-tail

    Both get and set count as a use and move the entry to the head.
    When capacity is exceeded, the tail (least recently used) is evicted.
    """

    def __init__(self, limit):
        if limit == 0:
            raise ValueError("limit must be greater than 0")
        self._limit = limit
        self._store = {}  # key → Node
        self._head = None
        self._tail = None

    def get(self, key):
        node = self._store.get(key)
        if node is None:
            return None
        self._move_to_head(node)
        return node.value

    def set(self, key, value):
        if key in self._store:
            node = self._store[key]
            node.value = value
            self._move_to_head(node)
        else:
            node = _Node(key, value)
            self._store[key] = node
            self._push_head(node)
            if len(self._store) > self._limit:
                self._evict_tail()

    def _push_head(self, node):
        node.prev = None
        node.next = self._head
        if self._head is not None:
            self._head.prev = node
        self._head = node
        if self._tail is None:
            self._tail = node

    def _unlink(self, node):
        if node.prev is not None:
            node.prev.next = node.next
        else:
            self._head = node.next
        if node.next is not None:
            node.next.prev = node.prev
        else:
            self._tail = node.prev
        node.prev = None
        node.next = None

    def _move_to_head(self, node):
        if node is self._head:
            return
        self._unlink(node)
        self._push_head(node)

    def _evict_tail(self):
        if self._tail is None:
            return
        del self._store[self._tail.key]
        self._unlink(self._tail)