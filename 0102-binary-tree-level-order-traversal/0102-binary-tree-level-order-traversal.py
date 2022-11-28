# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        level = [root]
        while level and root:
            result.append([x.val for x in level])
            level = [c for x in level for c in [x.left, x.right] if c]
        return result