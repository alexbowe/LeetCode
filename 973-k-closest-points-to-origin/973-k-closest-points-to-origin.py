class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def d(x):
            return x[0]**2 + x[1]**2
        
        import heapq
        
        heap = []
        for x in points:
            heapq.heappush(heap, (-d(x), x))
            if len(heap) > k:
                heapq.heappop(heap)
        
        return [x for _,x in heap]