class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        c = collections.Counter(nums)
        nums[:] = []
        for color, count in sorted(c.items()):
            nums.extend([color]*count)
        return nums