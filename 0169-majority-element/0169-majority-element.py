class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority = None
        count = 0
        for x in nums:
            if count == 0:
                majority = x
            count += 1 if x == majority else -1
        return majority