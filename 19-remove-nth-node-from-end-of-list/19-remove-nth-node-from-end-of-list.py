# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        n = n+1
        head = ListNode(next=head)
        slow, fast = head, head
        while fast:
            fast = fast.next
            if n == 0:
                slow = slow.next
            n = max(0,n-1)
            
        slow.next = slow.next.next if slow.next else None
        return head.next