class Solution:
    def longestPalindrome(self, s: str) -> int:
        c = collections.Counter(s)

        """
        ccc -> 3
        if odd, a
        """

        even = 0
        odd = 0
        for x,count in c.items():
            even += count//2
            odd += count%2
        return 2*even + (odd>0)