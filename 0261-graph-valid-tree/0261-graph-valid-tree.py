def is_tree(g):
    # Acyclic
    # Connected
    frontier = {0}
    seen = {0}

    while frontier:
        curr = frontier.pop()
        while g[curr]:
            n = g[curr].pop()
            if n in seen: continue
            frontier.add(n)
            seen.add(n)
        del g[curr]
    return not g

def make_graph(n, edges):
    g = {v:set() for v in range(n)}
    for u,v in edges:
        g[u].add(v)
        g[v].add(u)
    return g

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        return len(edges)==n-1 and is_tree(make_graph(n,edges))