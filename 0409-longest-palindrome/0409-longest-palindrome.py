class Solution:
    def longestPalindrome(self, s: str) -> int:
        c = Counter(s)
        even = sum(x//2 for x in c.values())
        odd  = sum(x%2  for x in c.values())
        return even*2 + (odd>0)