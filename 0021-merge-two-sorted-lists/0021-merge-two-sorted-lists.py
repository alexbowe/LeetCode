# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        prev = head

        while list1 and list2:
            list1, list2 = sorted([list1,list2], key=lambda x:x.val)
            prev.next = list1
            prev = list1
            list1 = list1.next
        
        curr = list1 if list1 else list2
        while curr:
            prev.next = curr 
            prev = curr
            curr = curr.next
        
        return head.next