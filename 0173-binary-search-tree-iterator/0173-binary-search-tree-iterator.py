# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def inorder(root):
    if not root: return
    yield from inorder(root.left)
    yield root
    yield from inorder(root.right)

class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self._it = (x.val for x in inorder(root))
        self._next = next(self._it, None)

    def next(self) -> int:
        x, self._next = self._next, next(self._it, None)
        return x

    def hasNext(self) -> bool:
        return self._next is not None


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()