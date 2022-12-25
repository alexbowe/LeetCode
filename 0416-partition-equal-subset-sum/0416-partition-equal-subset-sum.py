class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sums = reduce(lambda xs,y:xs|{y+x for x in xs}, nums, {0})
        return sum(nums)/2 in sums