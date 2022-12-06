# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        from heapq import merge
        def list_iter(xs):
            while xs:
                yield xs
                xs = xs.next
        
        merged = merge(*[list_iter(l) for l in lists], key=lambda x: x.val)
        
        head = ListNode()
        prev = head
        for x in merged:
            prev.next = x
            prev = x
        
        return head.next