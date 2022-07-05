# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n
        while left < right:
            x = left + (right - left)//2
            if isBadVersion(x):
                right = x
            else:
                left = x+1
        return left