class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def make_graph(num_nodes, edges):
            g = {i:{"in":set(),"out":set()} for i in range(num_nodes)}
            for u,v in edges:
                g[u]["out"].add(v)
                g[v]["in"].add(u)
            return g
        
        def find_start_point(g):
            for v,node in g.items():
                if not node["in"]: return v
                
        def delete_node(g, u):
            if u not in g: return
            for v in g[u]["out"]:
                g[v]["in"].remove(u)
                
            for v in g[u]["in"]:
                g[v]["out"].remove(u)
            
            del g[u]
            return g
            
        g = make_graph(numCourses, prerequisites)
        while g:
            i = find_start_point(g)
            if i is None: return False
            g = delete_node(g, i)
        
        return True
            
        