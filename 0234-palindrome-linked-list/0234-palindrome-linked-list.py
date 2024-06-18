# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
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
      
      tail = reverse_list(slow)

      return all(x.val==y.val for x,y in zip(iter_list(head), iter_list(tail)))