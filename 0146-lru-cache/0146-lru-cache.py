class ListNode:
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None
    
    def disconnect(self):
        if self.prev: self.prev.next = self.next
        if self.next: self.next.prev = self.prev
        self.prev = None
        self.next = None
    
    def postinsert(self, x):
        x.prev = self
        x.next = self.next
        if self.next: self.next.prev = x
        self.next = x

class LRUCache:

    def __init__(self, capacity: int):
        self._capacity = capacity
        self._d = dict()
        self._list_head = ListNode()
        self._list_tail = ListNode()
        self._list_head.postinsert(self._list_tail)

    def get(self, key: int) -> int:
        if key not in self._d: return -1
        node = self._d[key]
        node.disconnect()
        self._list_head.postinsert(node)
        return node.val
    
    def _evict(self):
        if not self._d: return
        node = self._list_tail.prev
        node.disconnect()
        del self._d[node.key]

    def put(self, key: int, value: int) -> None:
        if self.get(key) != -1:
            self._d[key].val = value
            return
        elif len(self._d) == self._capacity: self._evict()
        self._d[key] = ListNode(key=key, val=value)
        self._list_head.postinsert(self._d[key])


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)