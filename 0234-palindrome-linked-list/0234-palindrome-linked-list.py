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

        def reverse(curr):
            prev = None
            while curr:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            return prev
        
        # Find middle
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse middle
        left, right = head, reverse(slow)

        # Match
        return all(
            a.val==b.val
            for a,b
            in zip(iter_list(left), iter_list(right))
        )