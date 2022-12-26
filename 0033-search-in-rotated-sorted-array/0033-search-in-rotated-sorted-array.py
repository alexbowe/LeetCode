class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums)-1
        while lo<=hi:
            mid = lo+(hi-lo)//2
            
            mid_left    = nums[0] <= nums[mid]            
            target_left = nums[0] <= target
            same_side   = mid_left == target_left
            sentinel    = float("inf") if target_left else -float("inf")
            x           = nums[mid] if same_side else sentinel
            
            if   x == target: return mid
            elif  x < target: lo += 1
            else            : hi -= 1
        return -1
