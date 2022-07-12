class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        def twoSum(xs, start, target):
            indices = dict()
            for i in range(start,len(xs)):
                d = target-xs[i]
                if d in indices:
                    yield (indices[d], i)
                indices[xs[i]] = i
        
        result = set()
        for i in range(len(nums)-1):
            for j,k in twoSum(nums, i+1, -nums[i]):
                result.add((nums[i], nums[j], nums[k]))
                
        return list(result)