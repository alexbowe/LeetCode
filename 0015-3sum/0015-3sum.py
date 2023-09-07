class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def twoSum(xs, start, target):
            lo,hi = start, len(xs)-1
            while lo<hi:
                s = xs[lo] + xs[hi]
                if   s < target: lo+=1
                elif s > target: hi-=1
                else:
                    yield (lo, hi)
                    lo+=1; hi-=1;
                    while lo<hi and xs[lo]==xs[lo-1]: lo+=1
        
        nums.sort()

        result = []
        for i in range(len(nums)-2):
            if i>0 and nums[i] == nums[i-1]: continue
            for j,k in twoSum(nums, i+1, -nums[i]):
                result.append([nums[i],nums[j], nums[k]])
        return result