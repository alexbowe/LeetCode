class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(nums, lo, hi):
            nums[lo:hi] = reversed(nums[lo:hi])
                
        N = len(nums)
        k %= N
        reverse(nums, 0, N)
        reverse(nums, 0, k)
        reverse(nums, k, N)