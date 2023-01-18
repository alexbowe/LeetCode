# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inorder(root):
            if not root: return
            yield from inorder(root.left)
            yield root
            yield from inorder(root.right)
        
        return next(n.val for i,n in enumerate(inorder(root),1) if i==k)