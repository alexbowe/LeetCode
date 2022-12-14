# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
            x
          [ 3, 9,20,15, 7]
          [ 9, 3,15,20, 7]
          
        1. Next item of preorder is current root - always get value from here
        2. Current root splits inorder in two
        3. Arrays need same size: split preorder at same position after popping
        """
        if not preorder or not inorder: return None
        node = TreeNode(preorder[0])
        i = inorder.index(preorder[0])
        node.left  = self.buildTree(preorder[1:i+1], inorder[:i])
        node.right = self.buildTree(preorder[i+1:],  inorder[i+1:])
        return node