class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums)-1
        while lo<=hi:
            mid = lo + (hi-lo)//2
            
            mid_on_left = nums[0] <= nums[mid]
            target_on_left = nums[0] <= target
            same_side = mid_on_left == target_on_left
            sentinel = float("inf") if target_on_left else -float("inf")
            num = nums[mid] if same_side else sentinel
            
            if num == target: return mid
            if num < target:  lo = mid+1
            else:             hi = mid-1
        return -1