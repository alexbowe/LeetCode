# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def helper(root):
            if not root: return True, 0
            
            left_balanced, left_height = helper(root.left)
            if not left_balanced: return False, 0
            
            right_balanced, right_height = helper(root.right)
            if not right_balanced: return False, 0
            
            return abs(left_height - right_height) <= 1, 1+max(left_height, right_height)
        
        result, _ = helper(root)
        return result