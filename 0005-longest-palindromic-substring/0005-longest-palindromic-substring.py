class Solution:
    def longestPalindrome(self, s: str) -> str:        
        table = [[False]*len(s) for _ in range(len(s))]
        
        # First Order Palindromes
        for i in range(len(s)):
            table[i][i] = True
        
        # Second Order Palindromes
        for i in range(1, len(s)):
            table[i-1][i] = s[i-1] == s[i]
        
        # Higher Order Palindromes
        # Needs to be done bottom-to-top because
        # Recurrence relation depends on rows below
        for i in reversed(range(len(s)-1)): # skip bottom row
            for j in range(i+2, len(s)):
                table[i][j] = s[i] == s[j] and table[i+1][j-1]
        
        # Find longest palindrome
        a, b = 0, 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                if table[i][j] and j-i > b-a: a,b = i,j
        
        return s[a:b+1]