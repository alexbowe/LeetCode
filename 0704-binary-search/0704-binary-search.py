class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        while left <= right:
            m = left + (right-left)//2
            if nums[m] == target: return m
            if target < nums[m]: right = m - 1
            else: left = m + 1
        return -1