class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
          horse
         012345
        r112234
        o221234
        s332223 -> 3
        """
        N,M = len(word1)+1, len(word2)+1

        dp = [[0]*N for _ in range(M)]
        dp[0][:] = range(N)
        for row in range(M): dp[row][0] = row

        for i,j in product(range(1,M),range(1,N)):
            dp[i][j] = min(
                dp[i-1][j-1] + (word2[i-1]!=word1[j-1]), # substitution
                dp[i][j-1] + 1, # insertion
                dp[i-1][j] + 1, # deletion
            )
        
        return dp[-1][-1]