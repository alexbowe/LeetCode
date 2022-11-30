class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        
        - Brute force O(N^3) time O(1) space
        
        - Recursively while saving solutions:
        - P(i,j) = s[i] == s[j] and P(i+1,j-1)
        - P(i,i) = True
        - P(i,i+1) = s[i] == s[i+1]
        
        5
        abcde
        abc
        bcd
        cde
        
        5-w+1
        """
        
        table = [[False]*len(s) for _ in range(len(s))]
        
        # Palindromes of order 1
        for i in range(len(s)):
            table[i][i] = True
        
        # Palindromes of order 2
        for i in range(1, len(s)):
            table[i-1][i] = s[i-1] == s[i]
        
        # Higher orders
        for i in reversed(range(len(s)-1)):
            for j in range(i+2, len(s)):
                table[i][j] = s[i] == s[j] and table[i+1][j-1]
        
        #print(table)
        
        # Find longest palindrome
        a, b = 0, 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                if table[i][j] and j-i > b-a: a,b = i,j
        
        return s[a:b+1]