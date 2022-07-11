from collections import Counter
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        c = collections.Counter(nums)
        return any(count>=2 for count in c.values())