def make_graph(n, edges):
    g = {v:set() for v in range(n)}
    for u,v in edges:
        g[u].add(v)
        g[v].add(u)
    return g

def is_connected(g):
    q = {0}
    while q:
        v = q.pop()
        if v not in g: continue
        q |= g[v]
        del g[v]
    return len(g) == 0

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        return len(edges) == n-1 and is_connected(make_graph(n,edges))