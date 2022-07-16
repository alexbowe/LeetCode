class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        temp = [1]
        for x in nums:
            temp.append(temp[-1]*x)
        
        right = 1
        for i in reversed(range(len(nums))):
            temp[i+1] = right * temp[i]
            right = right * nums[i]
        
        return temp[1:]