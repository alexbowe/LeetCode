"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return None
        
        out_nodes = dict()
        stack = [node]
        while stack:
            curr = stack.pop()
            if curr.val not in out_nodes: out_nodes[curr.val] = Node(val=curr.val)
            for n in curr.neighbors:
                if n.val not in out_nodes:
                    out_nodes[n.val] = Node(val=n.val)
                    stack.append(n)
                out_nodes[curr.val].neighbors.append(out_nodes[n.val])
        
        return out_nodes[node.val]