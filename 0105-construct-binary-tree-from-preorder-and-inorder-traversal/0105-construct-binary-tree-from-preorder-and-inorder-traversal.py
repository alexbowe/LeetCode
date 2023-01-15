# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder: return None
        x = preorder[0]
        i = inorder.index(x)
        return TreeNode(
            x,
            self.buildTree(preorder[1:i+1], inorder[:i]),
            self.buildTree(preorder[i+1:], inorder[i+1:]),
        )