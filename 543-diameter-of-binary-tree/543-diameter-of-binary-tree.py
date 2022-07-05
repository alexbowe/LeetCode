# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
                         1
                 2               3
             4       5       6       7
           8   9   A   B   C   D   E   F
          G H I J K L M N O P Q R S T U V
        """
        def helper(root):
            # Return height, max_diameter
            if not root: return (0,0)
            
            left_height, left_diameter = helper(root.left)
            right_height, right_diameter = helper(root.right)
            
            height = 1+max(left_height, right_height)
            diameter = max(left_diameter, right_diameter, left_height + right_height)
            return height, diameter
        
        _, diameter = helper(root)
        return diameter
            
        
        