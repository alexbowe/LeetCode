# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        """
        
        def helper(root):
            if not root: return (0, 0)
            
            dl, hl = helper(root.left)
            dr, hr = helper(root.right)
            
            h = max(hl, hr) + 1
            d = max(dl, dr, hl+hr)
            return (d, h)
        
        d, _ = helper(root)
        return d