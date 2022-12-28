class Solution:
    def longestPalindrome(self, s: str) -> str:
        N = len(s)
        P = [[False] * N for _ in range(N)]
        
        for i in range(N):
            P[i][i] = True
            if i+1<N: P[i][i+1] = s[i] == s[i+1]
        
        for i in reversed(range(N)):
            for j in range(i+2, N):
                P[i][j] = s[i] == s[j] and P[i+1][j-1]
        
        a,b = 0,0
        for i in range(N):
            for j in range(i,N):
                if P[i][j] and j-i>=b-a: a,b=i,j
        return s[a:b+1]