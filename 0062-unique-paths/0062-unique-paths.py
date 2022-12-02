class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        - m + n - 2 = the total number of downs/rights (the required length of the path)
        - n - 1 - choose which positions to move to right
        """
        return math.comb(m + n - 2, n - 1)