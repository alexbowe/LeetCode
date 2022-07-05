# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        """
              B B B B B
        1 2 3 4 5 6 7 8
        L             R
              x
            R
          x
            L
            x
          R
        
        """
        left, right = 1, n
        while left<=right:
            x = left + (right - left)//2
            if isBadVersion(x):
                right = x-1
            else:
                left = x+1
        return left