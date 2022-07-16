# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        result = []
        level = [root]
        while level:
            result.append(level[-1].val)
            level = [c for x in level for c in [x.left, x.right] if c]
        return result