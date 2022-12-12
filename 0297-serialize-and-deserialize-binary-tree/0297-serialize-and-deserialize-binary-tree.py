# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root: return "#"
        return f"{root.val} {self.serialize(root.left)} {self.serialize(root.right)}"
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def helper(data = iter(data.split())):
            val = next(data)
            if val == "#": return None
            node = TreeNode(int(val))
            node.left = helper(data)
            node.right = helper(data)
            return node
        return helper()

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))