class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = nums[0]
        current = nums[0]
        for x in nums[1:]:
            current = max(current + x, x)
            result = max(result, current)
        return result