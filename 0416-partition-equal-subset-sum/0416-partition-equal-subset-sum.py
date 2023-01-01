class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sums = reduce(lambda xs,x: xs|{p+x for p in xs}, nums, {0})
        return sum(nums)/2 in sums