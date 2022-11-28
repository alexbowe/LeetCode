class Solution:
    def longestPalindrome(self, s: str) -> int:
        from collections import Counter
        c = Counter(s)
        even = sum(n//2 for n in c.values())
        odd = sum(n%2 for x,n in c.items())
        return even*2 + (odd>0)