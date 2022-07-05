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
        nodes = dict()
        neighbors = dict()
        stack = [node]
        
        while stack:
            curr = stack.pop()
            if curr.val in nodes: continue
            
            nodes[curr.val] = Node(val = curr.val)
            neighbors[curr.val] = [x.val for x in curr.neighbors]
            
            stack.extend(curr.neighbors)
        
        for v,ns in neighbors.items():
            nodes[v].neighbors = [nodes[n] for n in ns]
        
        return nodes[node.val]