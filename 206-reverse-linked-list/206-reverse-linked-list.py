# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        1 2 3 4 5
        
        """
        def helper(curr):
            if not curr: return (None, None)
            if not curr.next: return (curr, curr)
            successor, head = helper(curr.next)
            successor.next = curr
            curr.next = None
            return (curr, head)
        
        _, head = helper(head)
        return head