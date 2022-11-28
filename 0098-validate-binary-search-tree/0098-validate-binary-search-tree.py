# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def inorder(root):
            if not root: return
            yield from inorder(root.left)
            yield root.val
            yield from inorder(root.right)
            
        def pairs(xs):
            import itertools as it
            a,b = it.tee(xs)
            next(b,None)
            return zip(a,b)
        
        return all(a<b for a,b in pairs(inorder(root)))