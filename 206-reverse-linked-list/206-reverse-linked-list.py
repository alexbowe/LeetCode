# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def helper(curr, prev=None):
            if not curr: return prev
            temp = curr.next
            curr.next = prev
            return helper(temp, curr)
        
        return helper(head)