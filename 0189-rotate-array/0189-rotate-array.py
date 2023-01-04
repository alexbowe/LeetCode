class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(xs,lo,hi):
            while lo<hi:
                xs[lo],xs[hi] = xs[hi],xs[lo]
                lo+=1
                hi-=1
        
        N=len(nums)
        k%=N
        reverse(nums,0,N-1)
        reverse(nums,0,k-1)
        reverse(nums,k,N-1)
        