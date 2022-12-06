class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1]
        for x in nums:
            output.append(output[-1]*x)
        
        right = 1
        for i in reversed(range(1,len(output))):
            output[i] = output[i-1] * right
            right *= nums[i-1]
        
        return output[1:]