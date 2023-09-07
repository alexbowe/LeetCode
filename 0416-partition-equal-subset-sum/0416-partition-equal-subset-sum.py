class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        subtotals = reduce(lambda xs,x: xs|{s+x for s in xs}, nums, {0})
        return sum(nums)/2 in subtotals