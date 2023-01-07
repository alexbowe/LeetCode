class Solution:
    def rob(self, nums: List[int]) -> int:
        a, b = 0, 0
        for x in nums:
            # skip b and rob this, or rob b as well
            a, b = b, max(a + x, b)          
        return b