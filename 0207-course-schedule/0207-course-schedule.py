class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def make_graph(n, edges):
            g = {v:{"outgoing": set(), "indegree": 0} for v in range(n)}
            for v,u in edges:
                g[u]["outgoing"].add(v)
                g[v]["indegree"] += 1
            return g
        
        g = make_graph(numCourses, prerequisites)
        starts = [v for v in g.keys() if g[v]["indegree"]==0]
        if g and not starts: return False
        
        while starts:
            new_starts = []
            for u in starts:
                for v in g[u]["outgoing"]:
                    g[v]["indegree"] -= 1
                    if g[v]["indegree"] == 0: new_starts.append(v)
                del g[u]
            starts = new_starts
            
        return not bool(g)