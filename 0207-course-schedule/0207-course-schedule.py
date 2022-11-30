class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:        
        def make_graph(prerequisites):
            from collections import defaultdict
            g = defaultdict(lambda: {"in": set(), "out": set()})
            for u,v in prerequisites:
                g[u]["in"].add(v)
                g[v]["out"].add(u)
            return g
        
        def find_indegree_zero(g):
            return [u for u in g.keys() if not g[u]["in"]]
            
        g = make_graph(prerequisites)
        sources = find_indegree_zero(g)
        
        while sources:
            u = sources.pop()
            while g[u]["out"]:
                v = g[u]["out"].pop()
                g[v]["in"].remove(u)
                if not g[v]["in"]: sources.append(v)
            if not g[u]["out"] and not g[u]["in"]: del g[u]
        
        return not g