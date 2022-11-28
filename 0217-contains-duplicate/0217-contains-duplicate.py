class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        from collections import Counter
        return any(x>1 for x in Counter(nums).values())