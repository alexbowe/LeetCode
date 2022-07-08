# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        p, q = sorted([p,q], key=lambda x:x.val)
        while root:
            if root.val < p.val:
                root = root.right
            elif q.val < root.val:
                root = root.left
            else:
                return root
        
        