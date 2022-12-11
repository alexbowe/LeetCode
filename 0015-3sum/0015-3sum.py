class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        def twoSum(nums, start, target):
            d = dict()
            for i in range(start, len(nums)):
                delta = target - nums[i]
                if delta in d: yield [d[delta], i]
                d[nums[i]] = i
        
        results = set()
        for i in range(len(nums)-2):
            for j,k in twoSum(nums, i+1, -nums[i]):
                results.add((nums[i], nums[j], nums[k]))
        return list(results)