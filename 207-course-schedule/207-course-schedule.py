class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def make_graph(n, edges):
            g = {i:{"in":set(), "out":set()} for i in range(n)}
            for u,v in edges:
                g[u]["out"].add(v)
                g[v]["in"].add(u)
            return g
        
        def find_indegree_0(g):
            result = []
            for v,node in g.items():
                if not node["in"]:
                    result.append(v)
            return result
        
        def del_node(g, v):
            for i in g[v]["in"]:
                g[i]["out"].remove(v)
            for o in g[v]["out"]:
                g[o]["in"].remove(v)
            del g[v]
            return g
        
        g = make_graph(numCourses, prerequisites)
        
        while g:
            roots = find_indegree_0(g)
            if not roots: return False
            for v in roots:
                del_node(g, v)
                
        return True
            