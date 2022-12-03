# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def helper(root):
            if not root: return False, False, root
            lp, lq, ln = helper(root.left)
            if lp and lq: return lp, lq, ln
            rp, rq, rn = helper(root.right)
            if rp and rq: return rp, rq, rn
            has_p = lp or rp or root == p
            has_q = lq or rq or root == q
            return has_p, has_q, root
        return helper(root)[-1]