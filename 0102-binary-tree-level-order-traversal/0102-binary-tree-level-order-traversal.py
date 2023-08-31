# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []

        result = []
        level = [root]
        while level:
            result.append([x.val for x in level])
            level = [
                n for x in level
                for n in [x.left, x.right]
                if n
            ]
        return result
            