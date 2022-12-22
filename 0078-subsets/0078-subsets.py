class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        return reduce(lambda xs,x: xs+[r+[x] for r in xs], nums, [[]])