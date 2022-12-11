class Solution:
    def sortColors(self, nums: List[int]) -> None:
        c = collections.Counter(nums)
        nums[:] = [0] * c[0] + [1] * c[1] + [2] * c[2]
        