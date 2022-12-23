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
        def helper(tokens):
            x = tokens.pop()
            if x == "#": return None
            node = TreeNode(int(x))
            node.left = helper(tokens)
            node.right = helper(tokens)
            return node
        return helper(data.split()[::-1])
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))