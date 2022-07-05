class Solution:
    def longestPalindrome(self, s: str) -> int:
        from collections import Counter
        c = Counter(s)
        
        doubles = 0
        singles = 0
        for x in c:
            doubles += c[x]//2
            singles += c[x]%2
        
        return doubles * 2 + (1 if singles > 0 else 0)