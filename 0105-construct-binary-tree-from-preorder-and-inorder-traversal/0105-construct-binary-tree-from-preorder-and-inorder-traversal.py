# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        0 1  2  3 4
        
        3 9 20 15 7  - pre
          .
        9 3 15 20 7  - in
        """
        if not preorder or not inorder: return None
        x = preorder[0]
        i = inorder.index(x)
        return TreeNode(
            val   = x,
            left  = self.buildTree(preorder[1:i+1], inorder[:i+1]),
            right = self.buildTree(preorder[i+1:], inorder[i+1:]),
        )