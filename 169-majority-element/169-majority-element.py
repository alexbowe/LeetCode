class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        major = None
        count = 0
        
        for x in nums:
            if count == 0:
                count = 1
                major = x
            elif x == major:
                count += 1
            else:
                count -= 1
                
        return major