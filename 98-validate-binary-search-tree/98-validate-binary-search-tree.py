# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from itertools import tee

def pairwise(xs):
    a,b = tee(xs)
    next(b, None)
    return zip(a,b)

def tree_iterator(root, expand):
    stack = [(False, root)]
    while stack:
        expanded, curr = stack.pop()
        if not curr: continue
        if expanded: yield curr
        else: stack.extend((x is curr, x) for x in reversed(expand(curr)))
            
inorder = lambda root: tree_iterator(root, lambda x: (x.left, x, x.right))

def is_ordered(xs):
    return all(x<y for x,y in pairwise(xs))

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return is_ordered(x.val for x in inorder(root))