class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        j<i -> False
        i==j -> True
        i==j+1 and s[i]==s[j] -> True
        s[i]==s[j] and P(i+1,j-1) -> True

          babad
        b 10100
        a  1010
        b   100
        a    10
        d     1
    
        """

        N = len(s)
        P = [[0]*N for _ in range(N)]

        for i in range(N):
            P[i][i] = 1

        for i in range(N-1):
            P[i][i+1] = int(s[i] == s[i+1])

        for i in range(N-2,-1,-1):
            for j in range(i+2,N):
                P[i][j] = P[i+1][j-1] * int(s[i]==s[j])

        # print("\n".join("".join(str(x) for x in row) for row in P))

        I,J = 0,0
        for i in range(N):
            for j in range(i, N):
                if P[i][j]==1 and j-i>J-I: I,J = i,j
        
        return s[I:J+1]