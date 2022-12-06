class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums)-1
        while lo<=hi:
            mid = lo+(hi-lo)//2
            
            same_side = (nums[0] <= nums[mid]) == (nums[0] <= target)
            sentinel = float("inf") if nums[0] <= target else -float("inf")
            num = nums[mid] if same_side else sentinel
            
            if num == target: return mid
            elif num < target: lo = mid+1
            else: hi = mid-1
        
        return -1