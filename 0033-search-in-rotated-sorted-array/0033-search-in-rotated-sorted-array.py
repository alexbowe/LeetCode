class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums)-1
        while lo<=hi:
            mid = lo + (hi-lo)//2
            
            target_left = nums[0] <= target
            mid_left = nums[0] <= nums[mid]
            same_side = target_left == mid_left
            sentinel = float("inf") if target_left else -float("inf")
            x = nums[mid] if same_side else sentinel
            
            if x == target: return mid
            if x < target: lo = mid+1
            else: hi = mid-1
        return -1