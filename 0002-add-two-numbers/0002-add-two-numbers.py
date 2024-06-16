# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        out = prev = ListNode()
        carry = 0
        while l1 and l2:
          val = l1.val + l2.val + carry
          carry = val//10
          prev.next = ListNode(val%10)
          prev = prev.next
          l1 = l1.next
          l2 = l2.next
        
        tail = l1 or l2
        while tail:
          val = tail.val + carry
          carry = val//10
          prev.next = ListNode(val%10)
          prev = prev.next
          tail = tail.next
        
        if carry:
          prev.next = ListNode(carry)
        
        return out.next