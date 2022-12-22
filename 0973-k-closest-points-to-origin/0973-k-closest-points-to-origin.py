class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        euclidean_distance_squared = lambda x: x[0]**2 + x[1]**2
        return heapq.nsmallest(k, points, key=euclidean_distance_squared)