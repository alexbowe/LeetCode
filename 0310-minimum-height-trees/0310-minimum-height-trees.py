class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        """
        BFS would help find the min height from a root but we dont know which
        root to start from. We could do BFS from each node, but we can do better.

        Or, you can think of it like dependency graph, and do a toposort.
        But toposort needs to start with nodes that have no incoming edges...
        We can however determine which nodes are leaves, and do the toposort
        in reverse.
        
        Then you need to break ties because multiple nodes could be the root.

        How do we know when we have reached that condition?
        How many can a graph have at most?

        Here is an example similar to the 2nd example in the question, except an
        additional node has been added in an attempt to give it 3 roots.
        
                 3 ---- 4 ---- 5
               / | \    |      |
              0  1  2   6      7

        However, this doesn't have 3 roots. In this case 4 is the root, as
        otherwise there is a path 3,4,5,7 (or a similar one from 5), which 
        is not the minimum height.

        For nodes to end up at the root level, they all need to be connected
        and have an equal length path to each other. Since this is a tree, this
        can only happen if there are 1 or 2 nodes.

        So, toposort from leaves until there are 1 or 2 remaining nodes, then
        return those.
        """
        def make_graph(n, edges):
            g = {v:set() for v in range(n)}
            for u,v in edges:
                g[u].add(v)
                g[v].add(u)
            return g
            
        g = make_graph(n, edges)

        leaves = [v for v in g.keys() if len(g[v])<=1]
        while len(g) > 2:
            new_leaves = []
            for v in leaves:
                u = g[v].pop() # must have 1 and only 1 neighbor
                g[u].remove(v)
                del g[v]
                if len(g[u]) == 1:
                    new_leaves.append(u)
            leaves = new_leaves
        return leaves
