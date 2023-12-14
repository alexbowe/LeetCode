class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def make_graph(edges):
            g = collections.defaultdict(lambda: {"indegree": 0, "outgoing": set()})
            for v,u in edges:
                g[v]["indegree"] += 1
                g[u]["outgoing"].add(v)
            return g
        
        g = make_graph(prerequisites)

        s = [v for v in g.keys() if g[v]["indegree"] == 0]
        while g and s:
            u = s.pop()
            for v in g[u]["outgoing"]:
                g[v]["indegree"] -= 1
                if g[v]["indegree"] == 0: s.append(v)
            del g[u]
        return not g