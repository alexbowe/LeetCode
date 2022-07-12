# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def helper(root):
            if not root: return (True, 0)
            lb, lh = helper(root.left)
            if not lb: return (False, lh)
            rb, rh = helper(root.right)
            if not rb: return (False, rb)
            b = lb and rb and abs(lh-rh) <= 1
            h = max(lh, rh) + 1
            return (b,h)
        b,_ = helper(root)
        return b