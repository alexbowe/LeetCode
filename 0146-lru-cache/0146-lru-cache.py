class ListNode:
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None
    
    def remove(self):
        if self.prev: self.prev.next = self.next
        if self.next: self.next.prev = self.prev
        self.prev = None
        self.next = None
        return self
    
    def post_insert(self, other):
        other.prev = self
        other.next = self.next
        if self.next: self.next.prev = other
        self.next = other
        return self

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.d = {}
        self.list_head = ListNode()
        self.list_tail = ListNode()
        self.list_head.post_insert(self.list_tail)

    def get(self, key: int) -> int:
        if key not in self.d: return -1
        node = self.d[key]
        node.remove()
        self.list_head.post_insert(node)
        return node.val
    
    def _pop(self):
        if not self.d: return
        del self.d[self.list_tail.prev.remove().key]

    def put(self, key: int, value: int) -> None:
        if self.get(key) != -1: self.d[key].val = value; return
        if len(self.d) == self.capacity: self._pop()
        self.d[key] = ListNode(key=key,val=value)
        self.list_head.post_insert(self.d[key])
        
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)