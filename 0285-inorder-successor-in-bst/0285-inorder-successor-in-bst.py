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
        
        prev = None
        for x in inorder(root):
            if prev == p: return x
            prev = x
        return None