class Solution:
    def rob(self, nums: List[int]) -> int:
        a,b = 0,0
        for x in nums:
            a,b = b,max(a+x,b)
        return b