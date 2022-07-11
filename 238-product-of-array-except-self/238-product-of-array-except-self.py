class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        y_i = x_0 * x_1 * ... x_(i-1) * x_(i+1) * ... * x_(N-1)
        
        O(N) time
        No use of division!
        
        xs :      1  2  3  4
        pm : (1)  1  2  6 24  (1)       
        sm :     24 24 12  4
        ans:     24 12  8  6
        ^ can be computed in a backwards pass
        
        ans[i] = pm[i-1] * sm[i+1] # O(N) extra space for pm or sm
        
        O(1) extra space:
        Two passes?
        
        """
        result = []
        
        left = 1
        for x in nums:
            left *= x
            result.append(left)
            
        right = 1
        for i in reversed(range(len(nums))):
            result[i] = (result[i-1] if i>0 else 1)*right
            right *= nums[i]
        
        return result