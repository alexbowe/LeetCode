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
            yield root
            yield from inorder(root.right)
        pairs = itertools.pairwise(x.val for x in inorder(root))        
        return all(a<b for a,b in pairs)

            