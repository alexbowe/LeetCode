class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = nums[0]
        current = nums[0]
        
        for x in nums[1:]:
            # if prefix sum is negative, dont add it to the current subarray
            current = max(current + x, x)
            result = max(result, current)
        return result
           