class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        def twoSum(nums, left, right, target):
            deltas = dict()
            for i in range(left, right):
                x = nums[i]
                delta = target - x
                if delta in deltas:
                    yield (deltas[delta],i)
                deltas[x] = i
        
        result = set()
        for i in range(len(nums)-1):
            if i > 0 and nums[i] == nums[i-1]: continue
            
            # find two numbers in remainder of list that add up to give -nums[i]
            target = -nums[i]
            for j,k in twoSum(nums, i+1, len(nums), target):
                result.add((nums[i], nums[j], nums[k]))
        return list(result)