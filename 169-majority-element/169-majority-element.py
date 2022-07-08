class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority = nums[0] 
        count = 1
        for x in nums:
            if x == majority:
                count += 1
            else:
                count -= 1
                if count == 0:
                    count = 1
                    majority = x
        return majority