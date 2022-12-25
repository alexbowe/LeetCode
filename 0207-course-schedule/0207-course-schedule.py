class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def make_graph(prerequisites):
            g = collections.defaultdict(lambda: {"indegree":0, "out": set()})
            for v,u in prerequisites:
                g[u]["out"].add(v)
                g[v]["indegree"]+=1
            return g
        
        g = make_graph(prerequisites)
        starts = {v for v,node in g.items() if node["indegree"] == 0}
        
        while starts:
            u = starts.pop()
            for v in g[u]["out"]:
                g[v]["indegree"]-=1
                if g[v]["indegree"] == 0: starts.add(v)
            del g[u]
        
        return not g