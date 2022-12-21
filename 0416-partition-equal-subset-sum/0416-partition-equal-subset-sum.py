class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sums = reduce(lambda xs,x: xs|{s+x for s in xs}, nums, {0})
        return sum(nums)/2 in sums