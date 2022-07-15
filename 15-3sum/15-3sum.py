class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        def twoSum(nums, start, target):
            diffs = dict()
            for i in range(start, len(nums)):
                d = target - nums[i]
                if d in diffs:
                    yield (diffs[d], i)
                diffs[nums[i]] = i
        
        result = set()
        for i in range(len(nums)-1):
            if i > 0 and nums[i] == nums[i-1]: continue
            
            for j,k in twoSum(nums, i+1, -nums[i]):
                result.add((nums[i], nums[j], nums[k]))
        
        return list(result)