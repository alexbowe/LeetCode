class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        deltas = dict()
        for i,x in enumerate(nums):
            delta = target-x
            if delta in deltas:
                return [deltas[delta],i]
            deltas[x] = i
        return []