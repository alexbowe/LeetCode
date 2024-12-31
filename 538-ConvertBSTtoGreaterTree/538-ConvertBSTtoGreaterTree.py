# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def reverse_inorder(root):
    if not root: return
    yield from reverse_inorder(root.right)
    yield root
    yield from reverse_inorder(root.left)
    
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        total = 0
        
        for node in reverse_inorder(root):
            total += node.val
            node.val = total
        
        return root