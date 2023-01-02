class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return reduce(int.__xor__, nums)^reduce(int.__xor__,range(len(nums)+1))