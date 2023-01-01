class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = [x**2 for x in nums if x < 0]
        right = [x**2 for x in nums if x >= 0]
        return heapq.merge(reversed(left), right)