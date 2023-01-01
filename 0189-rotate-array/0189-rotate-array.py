class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def rev(xs, lo, hi):
            while lo<hi:
                xs[lo], xs[hi] = xs[hi], xs[lo]
                lo+=1; hi-=1
        N = len(nums)
        k %= N
        rev(nums,0,N-k-1)
        rev(nums,N-k,N-1)
        rev(nums,0,N-1)