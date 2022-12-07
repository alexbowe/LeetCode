class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        from heapq import nsmallest
        dist = lambda x: x[0]**2 + x[1]**2
        return nsmallest(k, points, key=dist)