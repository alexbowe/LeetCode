# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        from heapq import merge
        
        def iter_list(xs):
            while xs:
                yield xs
                xs = xs.next
        
        merged = merge(*[iter_list(list1), iter_list(list2)], key=lambda x:x.val)
        
        head = ListNode()
        prev = head
        for x in merged:
            prev.next = x
            prev = x
        
        return head.next