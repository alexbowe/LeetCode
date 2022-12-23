class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        def twoSum(nums, start, target):
            d = dict()
            for i in range(start, len(nums)):
                diff = target - nums[i]
                if diff in d: yield [d[diff], i]
                else: d[nums[i]] = i
        
        result = set()
        for i in range(len(nums)-2):
            for j,k in twoSum(nums, i+1, -nums[i]):
                result.add((nums[i],nums[j],nums[k]))
        return list(result)