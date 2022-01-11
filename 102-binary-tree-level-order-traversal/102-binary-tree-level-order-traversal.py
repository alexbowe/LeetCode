# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        
        result = []
        level = []
        curr_q = deque([root])
        next_q = deque([])
        
        while curr_q:
            curr = curr_q.popleft()
            level.append(curr.val)
            if curr.left: next_q.append(curr.left)
            if curr.right: next_q.append(curr.right)
            
            if not curr_q:
                result.append(level)
                level = []
                curr_q, next_q = next_q, curr_q
        
        return result