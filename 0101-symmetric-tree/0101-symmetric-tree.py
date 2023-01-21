# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def helper(p, q):
            if not p or not q: return bool(p) == bool(q)
            return p.val == q.val and helper(p.left, q.right) and helper(p.right, q.left)
        return not root or helper(root.left, root.right)