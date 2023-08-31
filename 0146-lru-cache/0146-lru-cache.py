class ListNode:
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

    def post_insert(self, other):
        other.prev = self
        other.next = self.next
        if self.next: self.next.prev = other
        self.next = other
        return other
    
    def disconnect(self):
        if self.prev: self.prev.next = self.next 
        if self.next: self.next.prev = self.prev
        self.prev = None
        self.next = None
        return self

class LRUCache:

    def __init__(self, capacity: int):        
        self._d = dict()
        self._capacity = capacity
        self._list_head = ListNode()
        self._list_tail = ListNode()
        self._list_head.post_insert(self._list_tail)
    
    def get(self, key: int) -> int:
        if key not in self._d: return -1
        return self._list_head.post_insert(self._d[key].disconnect()).val
    
    def _pop_right(self):
        del self._d[self._list_tail.prev.disconnect().key]

    def put(self, key: int, value: int) -> None:
        if self.get(key) != -1:
            self._d[key].val = value
            return
        
        if len(self._d) == self._capacity:
            self._pop_right()
        
        self._d[key] = self._list_head.post_insert(ListNode(key=key, val=value))


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)