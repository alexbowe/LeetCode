class Solution:
    def longestPalindrome(self, s: str) -> int:
        from collections import Counter
        c = Counter(s)
        even = sum(n//2 for n in c.values())
        odds = sum(1 for x,n in c.items() if n%2==1)
        return even*2 + (odds>0)