# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = slow = head
        while fast and n:
            fast = fast.next
            n-=1
        if not fast: return head.next
        while slow.next and fast.next:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return head