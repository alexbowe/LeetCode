class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def make_graph(n, edges):
            g = {i:{"in":set(), "out":set()} for i in range(n)}
            for u,v in edges:
                g[u]["out"].add(v)
                g[v]["in"].add(u)
            return g
        
        def find_indegree_zero(g):
            if not g: return []
            xs = []
            for u in g.keys():
                if not g[u]["in"]:
                    xs.append(u)
            return xs
        
        def del_node(g, v):
            for n in g[v]["in"]:
                g[n]["out"].remove(v)
            for n in g[v]["out"]:
                g[n]["in"].remove(v)
            del g[v]
            return g
        
        g = make_graph(numCourses, prerequisites)
        starts = find_indegree_zero(g)
        while starts:
            for v in starts:
                del_node(g, v)
            starts = find_indegree_zero(g)
        return not g