class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        def key(value):
            return abs(x-value)
        return sorted(heapq.nsmallest(k, arr, key=key))