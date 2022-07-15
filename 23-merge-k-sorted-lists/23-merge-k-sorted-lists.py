# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def iter_lists(curr):
            while curr:
                yield curr
                curr = curr.next
        
        prev = dummy = ListNode()
        for x in heapq.merge(*map(iter_lists, lists), key=lambda x:x.val):
            prev.next = x
            prev = x
        return dummy.next
        