# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        Observations:
        - preorder = [root][preorder_left][preorder_right]
        - inorder  = [inorder_left][root][inorder_right]
        - Dont know value of root from inorder, but preorder tells us that.
        - Dont know size of preorder_left or right, but inorder tells us that.
        """
        assert len(preorder) == len(inorder)
        if not preorder or not inorder: return None
        root_val = preorder[0]
        root_pos = inorder.index(root_val)        
        return TreeNode(
            val = root_val,
            left = self.buildTree(preorder[1:1+root_pos],inorder[:root_pos]),
            right = self.buildTree(preorder[1+root_pos:],inorder[root_pos+1:]),
        )
