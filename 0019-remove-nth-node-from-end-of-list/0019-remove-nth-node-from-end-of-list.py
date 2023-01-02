# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def iterlist(head):
            while head: yield head; head = head.next
        
        N = sum(1 for x in iterlist(head))
        
        dummy = ListNode()
        prev = dummy
        for i,x in enumerate(iterlist(head),1):
            if i == N-n+1: continue
            prev.next = x
            prev = x
        prev.next = None
        return dummy.next