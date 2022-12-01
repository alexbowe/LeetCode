class Solution:
    def sortColors(self, nums: List[int]) -> None:
        c = collections.Counter(nums)
        nums[:] = []
        for color, count in sorted(c.items()):
            nums.extend([color]*count)