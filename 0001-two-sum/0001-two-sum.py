class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diffs = dict()
        for i,x in enumerate(nums):
            d = target - x
            if d in diffs:
                return [diffs[d], i]
            diffs[x] = i
        return None