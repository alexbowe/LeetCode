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
        def helper(curr, prev=None):
            if not curr: return None
            temp = curr.next
            curr.next = prev
            if not temp: return curr
            return helper(temp, curr)
        
        return helper(head)