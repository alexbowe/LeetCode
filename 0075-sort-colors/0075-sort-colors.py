class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        c = collections.Counter(nums)
        nums[:] = [0]*c[0] + [1]*c[1] + [2]*c[2]