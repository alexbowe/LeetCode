class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        """
         1 5 11 5
        
        How would I brute force it?
        Try every partition and sum them up and compare
        - Get total. Partition sum should be total/2. Total hence needs to be even.
        - Find the subset of elements that add to give total/2
        """
        total = sum(nums)
        if total%2 != 0: return False
        sums = {0}
        for n in nums:
            sums |= {(s+n) for s in sums}
        return total//2 in sums