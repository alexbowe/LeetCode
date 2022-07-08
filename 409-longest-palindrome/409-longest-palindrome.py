class Solution:
    def longestPalindrome(self, s: str) -> int:
        from collections import Counter
        counts = Counter(s)
        
        doubles = 0
        singles = 0
        for x in counts:
            doubles += counts[x]//2
            singles += counts[x]%2
        
        return 2*doubles + min(singles,1)