class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = [x*x for x in nums if x < 0][::-1]
        right = [x*x for x in nums if x >= 0]
        return heapq.merge(left,right)