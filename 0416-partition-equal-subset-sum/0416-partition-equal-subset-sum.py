class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total%2 != 0: return False
        sums = reduce(lambda xs,x: xs | {s + x for s in xs}, nums, {0})
        return total//2 in sums