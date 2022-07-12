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
        
        root_key = node.val
        nodes = {}
        edges = {}
        stack = [node]
        
        while stack:
            curr = stack.pop()
            nodes[curr.val] = Node(val=curr.val)
            edges[curr.val] = [n.val for n in curr.neighbors]
            
            for n in curr.neighbors:
                if n.val in nodes: continue
                stack.append(n)
        
        for v in nodes.keys():
            nodes[v].neighbors = [nodes[n] for n in edges[v]]
        
        return nodes[root_key]