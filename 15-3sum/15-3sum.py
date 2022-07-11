class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        def twoSum(nums, start, target):
            deltas = dict()
            for j in range(start, len(nums)):
                x = nums[j]
                delta = target - x
                if delta in deltas:
                    yield (deltas[delta], j)
                deltas[x] = j
        
        result = set()
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]: continue
                
            target = -nums[i]
            for j,k in twoSum(nums, i+1, target):
                if i in (j,k): continue
                result.add((nums[i],nums[j],nums[k]))
        
        return list(result)