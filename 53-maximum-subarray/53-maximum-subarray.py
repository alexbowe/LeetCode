class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current = nums[0]
        max_sum = nums[0]
        for x in nums[1:]:
            current = max(x, current+x)
            max_sum = max(max_sum, current)
        return max_sum