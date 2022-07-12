# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def iterate_list(curr):
            while curr:
                temp = curr
                curr = curr.next
                yield temp
        
        prev = dummy = ListNode()
        for x in heapq.merge(*(iterate_list(l) for l in lists), key=lambda x:x.val):
            prev.next = x
            prev = x
        
        return dummy.next