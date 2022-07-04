# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(root):
            stack = [(1, root)]
            max_height = 0
            while stack:
                h, curr = stack.pop()
                max_height = max(max_height, h)
                if not curr: continue
                stack.extend([(h+1, curr.left), (h+1, curr.right)])
            return max_height
        
        if not root: return True
        return self.isBalanced(root.left) and self.isBalanced(root.right) and abs(height(root.left) - height(root.right)) <= 1