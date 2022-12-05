class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def helper(partial, nums):
            if not nums: yield partial
            for i in range(len(nums)):
                yield from helper(partial+[nums[i]], nums[:i] + nums[i+1:])
        return list(helper([], nums))