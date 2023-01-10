class ListNode:
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None
        
    def remove(self):
        if self.prev: self.prev.next = self.next
        if self.next: self.next.prev = self.prev
        self.prev = None
        self.next = None
        return self
    
    def postinsert(self, other):
        other.prev = self
        other.next = self.next
        if self.next: self.next.prev = other
        self.next = other
        return self

class LRUCache:

    def __init__(self, capacity: int):
        self._capacity = capacity
        self._d = dict()
        self._head = ListNode()
        self._tail = ListNode()
        self._head.postinsert(self._tail)

    def get(self, key: int) -> int:
        if key not in self._d: return -1
        return self._head.postinsert(self._d[key].remove()).next.val

    def put(self, key: int, value: int) -> None:
        if self.get(key) != -1: self._d[key].val = value; return
        if len(self._d) == self._capacity: del self._d[self._tail.prev.remove().key]
        self._d[key] = self._head.postinsert(ListNode(key,value)).next
            


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)