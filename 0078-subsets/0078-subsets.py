class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums: return []
        result = [[]]
        for x in nums:
            result += [r + [x] for r in result]
        return result