# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        level = [root]
        result = []
        while level and root:
            result.append(level[-1].val)
            new_level = []
            for node in level:
                if node.left: new_level.append(node.left)
                if node.right: new_level.append(node.right)
            level = new_level
        return result