# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        indices = {x:i for i,x in enumerate(inorder)}
        if not preorder or not inorder: return None
        node = TreeNode(preorder[0])
        i = indices[preorder[0]]
        node.left = self.buildTree(preorder[1:i+1],inorder[:i])
        node.right = self.buildTree(preorder[i+1:],inorder[i+1:])
        return node