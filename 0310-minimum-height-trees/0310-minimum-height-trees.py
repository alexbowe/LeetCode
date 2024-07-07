class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        def build_graph(n, edges):
            g = {v:set() for v in range(n)}
            for u,v in edges:
                g[u].add(v)
                g[v].add(u)
            return g

        g = build_graph(n, edges)

        leaves = {v for v in g.keys() if len(g[v]) <= 1}

        while len(g)>2:
            new_leaves = set()
            for u in leaves:
                for v in g[u]:
                    g[v].remove(u)
                    if len(g[v]) <= 1: new_leaves.add(v)
                del g[u]
            leaves = new_leaves
        
        return leaves