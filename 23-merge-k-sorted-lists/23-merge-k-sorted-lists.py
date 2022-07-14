# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def iter_list(curr):
            while curr:
                yield curr
                curr = curr.next
        
        prev = dummy = ListNode()
        for n in heapq.merge(*map(iter_list,lists), key=lambda x:x.val):
            prev.next = n
            prev = n
            
        return dummy.next