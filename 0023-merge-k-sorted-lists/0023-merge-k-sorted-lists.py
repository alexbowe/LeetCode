# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def iterlist(xs):
            while xs:
                yield xs
                xs = xs.next
        
        merged = heapq.merge(*[iterlist(xs) for xs in lists], key=lambda x:x.val)
        
        head = ListNode()
        prev = head
        for curr in merged:
            prev.next = curr
            prev = curr
            curr = curr.next
        return head.next