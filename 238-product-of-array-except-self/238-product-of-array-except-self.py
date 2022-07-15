class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        
         1  2  3  4
         1  2  6 24
              12  4 1
              
        24 12  8  6
        
        """
        left = 1
        temp = [1]
        for i in range(len(nums)):
            left = left * nums[i]
            temp.append(left)
        
        right = 1
        for i in reversed(range(len(nums))):
            temp[1+i] = temp[i] * right
            right = right * nums[i]
            
        return temp[1:]