class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # From m + n - 2 directions, choose n - 1 moves to the right
        return math.comb(m+n-2, n-1)