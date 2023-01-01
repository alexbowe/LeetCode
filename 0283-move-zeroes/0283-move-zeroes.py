class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        N = len(nums)
        nums[:] = (x for x in nums if x!=0)
        nums.extend([0]*(N-len(nums)))