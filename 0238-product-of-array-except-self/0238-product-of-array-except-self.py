class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1]
        for x in nums:
            result.append(result[-1] * x)
        
        right = 1
        for i in reversed(range(1,len(result))):
            result[i] = result[i-1] * right
            right *= nums[i-1]
        
        return result[1:]