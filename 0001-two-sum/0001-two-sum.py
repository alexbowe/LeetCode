class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = dict()
        for i,x in enumerate(nums):
            diff = target - x
            if diff in d:
                return [d[diff], i]
            d[x] = i
        return []