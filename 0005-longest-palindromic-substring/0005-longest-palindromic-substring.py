class Solution:
    def longestPalindrome(self, s: str) -> str:
        table = [[False]*len(s) for _ in range(len(s))]
        
        for i in range(len(s)):
            table[i][i] = True
        
        for i in range(len(s)-1):
            table[i][i+1] = s[i] == s[i+1]
        
        for i in reversed(range(len(s)-1)):
            for j in range(i+2, len(s)):
                table[i][j] = s[i] == s[j] and table[i+1][j-1]
                    
        a,b = 0,0
        for i in range(len(s)):
            for j in range(i, len(s)):
                if j-i > b-a and table[i][j]: a,b = i,j
        
        return s[a:b+1]