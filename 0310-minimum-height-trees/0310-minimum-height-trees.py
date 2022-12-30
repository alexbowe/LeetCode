class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        def make_graph(n, edges):
            g = {i:set() for i in range(n)}
            for u,v in edges:
                g[u].add(v)
                g[v].add(u)
            return g
        
        g = make_graph(n, edges)
        leaves = [v for v,neighbors in g.items() if len(neighbors)<=1]
        
        while len(g)>2:
            new_leaves = []
            for v in leaves:
                u = g[v].pop()
                g[u].remove(v)
                del g[v]
                if len(g[u]) == 1: new_leaves.append(u)
            leaves = new_leaves
        
        return leaves