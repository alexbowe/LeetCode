class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        def make_graph(n, edges):
            g = {i:set() for i in range(n)}
            for u,v in edges:
                g[u].add(v)
                g[v].add(u)
            return g
        g = make_graph(n,edges)
        
        leaves = [u for u,neighbors in g.items() if len(neighbors)<=1]
        
        while len(g) > 2:
            new_leaves = []
            for u in leaves:
                v = g[u].pop()
                g[v].remove(u)
                del g[u]
                if len(g[v]) == 1: new_leaves.append(v)
            leaves = new_leaves
        
        return leaves