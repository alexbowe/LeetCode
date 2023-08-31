# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def helper(root):
            if not root: return 0, 0
            lh, ld = helper(root.left)
            rh, rd = helper(root.right)
            return max(lh,rh)+1, max(lh+rh, ld, rd)
        return helper(root)[-1]