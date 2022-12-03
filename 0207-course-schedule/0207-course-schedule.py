class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def make_graph(prerequisites):
            g = collections.defaultdict(lambda: {"incoming": set(), "outgoing": set()})
            for u,v in prerequisites:
                g[u]["incoming"].add(v)
                g[v]["outgoing"].add(u)
            return g    
        
        def find_indegree_zero(g):
            return {u for u in g.keys() if not g[u]["incoming"]}
        
        g = make_graph(prerequisites)
        starts = find_indegree_zero(g)
        while starts:
            # delete all outgoing edges u,v
            u = starts.pop()
            while g[u]["outgoing"]:
                v = g[u]["outgoing"].pop()
                g[v]["incoming"].remove(u)
                if not g[v]["incoming"] and not g[v]["outgoing"]: del g[v]
                elif not g[v]["incoming"]: starts.add(v)
            if not g[u]["incoming"] and not g[u]["outgoing"]: del g[u]
        
        print(g)
        return len(g) == 0