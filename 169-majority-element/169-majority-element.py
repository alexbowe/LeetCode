class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        major = nums[0]
        count = 1
        
        for x in nums[1:]:
            if x != major:
                count -= 1
                if count == 0:
                    major = x
                    count = 1
            else:
                count += 1
                
        return major