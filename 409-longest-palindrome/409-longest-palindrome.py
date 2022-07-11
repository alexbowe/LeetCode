class Solution:
    def longestPalindrome(self, s: str) -> int:
        c = collections.Counter(s)
        doubles = 0
        singles = 0
        for _,count in c.items():
            doubles += count//2
            singles += count%2
        return 2*doubles + (1 if singles > 0 else 0)