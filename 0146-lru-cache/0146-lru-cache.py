class ListNode:
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None
        
    def disconnect(self):
        if self.prev: self.prev.next = self.next
        if self.next: self.next.prev = self.prev
        self.next = None
        self.prev = None
    
    def post_insert(self, other):
        other.next = self.next
        other.prev = self
        if self.next: self.next.prev = other
        self.next = other

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.d = dict()
        self.list_head = ListNode()
        self.list_tail = ListNode()
        self.list_head.next = self.list_tail
        self.list_tail.prev = self.list_head

    def get(self, key: int) -> int:
        if key not in self.d: return -1
        node = self.d[key]
        node.disconnect()
        self.list_head.post_insert(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        self.get(key)
        
        if key in self.d:
            self.d[key].val = value
            return
        
        if len(self.d) == self.capacity:
            del self.d[self.list_tail.prev.key]
            self.list_tail.prev.disconnect()
            
        self.d[key] = ListNode(key=key,val=value)
        self.list_head.post_insert(self.d[key])


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)