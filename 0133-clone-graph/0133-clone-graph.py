"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        def helper(curr, nodes=None):
            if not curr: return None
            nodes = nodes or dict()
            if curr.val in nodes: return nodes[curr.val]

            new_node = nodes.setdefault(curr.val, Node(curr.val))
            for n in curr.neighbors:
                new_node.neighbors.append(helper(n, nodes))
            return new_node
        return helper(node)
