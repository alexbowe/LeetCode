class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def make_graph(prerequisites):
            g = collections.defaultdict(lambda: {"out": set(), "indegree": 0})
            for course,prereq in prerequisites:
                g[course]["indegree"] += 1
                g[prereq]["out"].add(course)
            return g
        
        g = make_graph(prerequisites)
        roots = [v for v,node in g.items() if node["indegree"] == 0]
        while roots:
            c = roots.pop()
            course = g[c]
            for out in course["out"]:
                g[out]["indegree"] -= 1
                if g[out]["indegree"] == 0: roots.append(out)
            del g[c]
        return not bool(g)
            
            