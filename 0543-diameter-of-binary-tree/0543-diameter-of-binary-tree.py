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
            ld, lh = helper(root.left)
            rd, rh = helper(root.right)
            d = lh + rh
            return max(ld, rd, d), max(lh, rh) + 1
        return helper(root)[0]