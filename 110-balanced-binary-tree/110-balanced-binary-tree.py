# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def helper(root):
            # balanced, height
            if not root: return True, 0
            lb, lh = helper(root.left)
            rb, rh = helper(root.right)
            b = lb and rb and abs(lh-rh)<=1
            h = 1 + max(lh, rh)
            return b,h
        balanced, _ = helper(root)
        return balanced