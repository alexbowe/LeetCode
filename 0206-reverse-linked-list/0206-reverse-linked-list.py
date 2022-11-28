# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def helper(prev, head):
            if not head: return prev
            temp = head.next
            head.next = prev
            return helper(head, temp)
            
        return helper(None, head)
            