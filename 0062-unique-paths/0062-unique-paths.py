class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        We have m-1 down and n-1 right moves to make, e.g. DDDRRRRR...
        How many combinations of those can we make?
        If we dont choose a down, we must choose a right -> binomial distribution.
        """
        return math.comb(m+n-2, n-1)
        