class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        complements = Counter([0])
        for x in accumulate(nums):
            ans += complements[x-k]
            complements[x] += 1
        return ans