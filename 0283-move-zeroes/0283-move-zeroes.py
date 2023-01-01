class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        N = len(nums)
        nums[:] = (x for x in nums if x != 0)
        n_zeros = N-len(nums)
        nums.extend((0 for _ in range(n_zeros)))