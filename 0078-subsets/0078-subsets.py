class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = [[]]
        for x in nums:
            result.extend([subset + [x] for subset in result])
        return result