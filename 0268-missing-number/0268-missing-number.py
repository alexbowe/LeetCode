class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return reduce(int.__xor__, itertools.chain(range(len(nums)+1),nums))