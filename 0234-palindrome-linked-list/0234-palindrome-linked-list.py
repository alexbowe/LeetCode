# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
      """
          
              f
      1 2 5 2 1
          s
      """
      def iter_list(curr):
        while curr:
          yield curr
          curr = curr.next

      def reverse_list(curr):
        prev = None
        while curr:
          temp = curr.next
          curr.next = prev
          prev = curr
          curr = temp
        return prev      
      
      fast = slow = head
      while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
      
      # Reverse slow (which is second half of list)
      tail = reverse_list(slow)

      for x,y in zip(iter_list(head), iter_list(tail)):
        if x.val != y.val: return False
      
      return True