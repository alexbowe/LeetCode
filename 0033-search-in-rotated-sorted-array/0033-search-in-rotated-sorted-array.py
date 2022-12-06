class Solution:
    def search(self, nums: List[int], target: int) -> int:            
        lo, hi = 0, len(nums)-1
        while lo<=hi:
            mid = lo + (hi-lo)//2
            
            # Use a pivot to see if mid and target would be in same half
            # - if nums[0] > mid, mid is not on the left half.
            # - if nums[0] > target, target is not on the left half.
            # - if same answer to both, mid and target on the same half.
            same_half = (nums[mid] < nums[0]) == (target < nums[0])
            # Sentinel value to replace the half that target is not in
            sentinel = -float("inf") if target < nums[0] else float("inf")
            num = nums[mid] if same_half else sentinel
            
            if num == target: return mid
            if num < target: lo = mid + 1
            else: hi = mid - 1
        return -1
            