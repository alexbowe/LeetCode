class Solution:
    def search(self, nums: List[int], target: int) -> int:
        pivot = bisect.bisect_left(nums, True, key=lambda x:x<=nums[-1])
        left  = bisect.bisect_left(nums, target, hi=pivot)
        right = bisect.bisect_left(nums, target, lo=pivot)

        if  left < len(nums) and nums[left]  == target: return left
        if right < len(nums) and nums[right] == target: return right
        return -1
