class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def twoSum(nums, start, target):
            d = dict()
            for i in range(start, len(nums)):
                x = nums[i]
                diff = target - x
                if diff in d: yield (d[diff], i)
                d[x] = i
        
        nums = sorted(nums)
        
        result = set()
        for i in range(len(nums)-2):
            for j,k in twoSum(nums, i+1, -nums[i]):
                result.add((nums[i], nums[j], nums[k]))
        
        return list(result)