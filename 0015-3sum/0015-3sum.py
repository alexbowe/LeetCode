class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        def twoSum(nums, start, target):
            diffs = dict()
            for i in range(start, len(nums)):
                x = nums[i]
                d = target - x
                if d in diffs:
                    yield (diffs[d], i)
                diffs[x] = i
        
        nums = sorted(nums)

        result = set()
        for i in range(len(nums)-2):
            x = nums[i]
            for j,k in twoSum(nums, i+1, -x):
                result.add((nums[i], nums[j], nums[k]))
        return list(result)