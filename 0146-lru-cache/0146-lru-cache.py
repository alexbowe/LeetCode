class ListNode:
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None
        
    def remove(self):
        if self.prev: self.prev.next = self.next
        if self.next: self.next.prev = self.prev
        self.next = None
        self.prev = None
        return self
        
    def postinsert(self, x):
        x.prev = self
        x.next = self.next
        if self.next: self.next.prev = x
        self.next = x
        return self
        
class LRUCache:

    def __init__(self, capacity: int):
        self._capacity = capacity
        self._d = dict()
        self._list_head = ListNode()
        self._list_tail = ListNode()
        self._list_head.postinsert(self._list_tail)

    def get(self, key: int) -> int:
        if key not in self._d: return -1
        node = self._d[key].remove()
        self._list_head.postinsert(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if self.get(key) != -1: self._d[key].val = value; return
        
        if len(self._d) == self._capacity:
            k = self._list_tail.prev.remove().key
            del self._d[k]
            
        self._d[key] = ListNode(key,value)
        self._list_head.postinsert(self._d[key])
            

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)