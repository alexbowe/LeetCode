# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def helper(root, p, q):
            if not root: return (False, False, None)
            left_has_p, left_has_q, left_node = helper(root.left, p, q)
            if left_has_p and left_has_q: return (True, True, left_node)
            right_has_p, right_has_q, right_node = helper(root.right, p, q)
            if right_has_p and right_has_q: return (True, True, right_node)
            root_has_p = (left_has_p or right_has_p or root.val == p.val)
            root_has_q = (left_has_q or right_has_q or root.val == q.val)
            print(f"({root.val}) return: {root_has_p}, {root_has_q}, {root.val}")
            return (root_has_p, root_has_q, root)
        
        _, _, node = helper(root, p, q)
        return node