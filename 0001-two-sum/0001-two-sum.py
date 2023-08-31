class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = dict()
        for i,x in enumerate(nums):
            delta = target-x
            if delta in d:
                return [d[delta], i]
            d[x] = i