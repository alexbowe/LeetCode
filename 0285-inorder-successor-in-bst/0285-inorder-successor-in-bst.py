# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        def inorder(root):
            if not root: return
            yield from inorder(root.left)
            yield root
            yield from inorder(root.right)
            
        found = False
        for x in inorder(root):
            if found: return x
            found = x == p
        return None