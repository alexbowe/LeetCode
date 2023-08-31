# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def helper(prev, curr):
            if not curr: return prev, curr
            temp = curr.next
            curr.next = prev
            return helper(curr, temp)
        return helper(None, head)[0]
    