class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def d(x):
            return x[0]**2 + x[1]**2
        
        import heapq
        
        heap = []
        for x in points:
            dist = d(x)
            if len(heap) + 1 > k:
                heapq.heappushpop(heap, (-dist, x))
            else:
                heapq.heappush(heap, (-dist, x))
        
        return [x for _,x in heap]