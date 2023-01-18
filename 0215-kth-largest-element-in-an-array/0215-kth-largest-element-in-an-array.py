class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return sorted(heapq.nlargest(k, nums))[0]