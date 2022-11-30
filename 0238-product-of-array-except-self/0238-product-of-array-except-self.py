class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        24 12  8  6   ans
         1  2  3  4   xs
       1 1  2  6 24   left
        24 24 12  4 1 right = 
        24 12  8  6   left_i * right_n-i
        
        """
        left = [1]
        for x in nums:
            left.append(left[-1]*x)
        
        right = 1
        for i in reversed(range(1, len(left))):
            left[i] = left[i-1] * right
            right *= nums[i-1]
        
        return left[1:]