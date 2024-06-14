class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        def twoSum(nums, start, target):
            for i in range(start, len(nums)-1):
                if i>start and nums[i-1]==nums[i]: continue
                j = bisect.bisect_left(nums, target-nums[i], lo=i+1)
                if j<len(nums) and nums[i]+nums[j]==target: yield (i,j)

        result = []
        for i in range(len(nums)-2):
            if i>0 and nums[i-1]==nums[i]: continue
            for j,k in twoSum(nums, i+1, -nums[i]):
                result.append((nums[i], nums[j], nums[k]))
        return result