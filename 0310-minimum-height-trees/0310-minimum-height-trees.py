class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 2: return list(range(n))
        
        def make_graph(edges):
            g = collections.defaultdict(set)
            for u,v in edges:
                g[u].add(v)
                g[v].add(u)
            return g
        
        g = make_graph(edges)
        
        leaves = [v for v,neighbors in g.items() if len(neighbors)==1]
        while len(g) > 2:
            new_leaves = []
            for v in leaves:
                u = g[v].pop()
                del g[v]
                g[u].remove(v)
                if len(g[u]) == 1: new_leaves.append(u)
            leaves = new_leaves
        return leaves