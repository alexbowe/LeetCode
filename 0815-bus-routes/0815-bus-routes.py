class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        """
        - route[i] is a bus route that bus i repeats forever
        - the routes loop forever


        start at bus stop source
        get to stop `target`

        Least number of buses you need to take to travel from source to target

        BFS


        """
        if source == target: return 0

        def make_graph(routes):
            g = defaultdict(set) # edge (stop) label to node (bus)
            for bus,route in enumerate(routes):
                for stop in route:
                    g[stop].add(bus)
            return g
        
        g = make_graph(routes)
        print("routes:",routes)
        print("graph:", g)

        cost = 0
        #visited = set()
        level = {*g[source]}
        seen = level.copy()

        while level:
            cost += 1
            new_level = set()
            for bus in level:
                for stop in routes[bus]:
                    if stop == target: return cost
                    new_level.update(bus for bus in g[stop] if bus not in seen)
                    seen.update(g[stop])
            level = new_level
        
        return -1
                    
        