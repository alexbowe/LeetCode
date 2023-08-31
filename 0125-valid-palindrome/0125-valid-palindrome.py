class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = [x.lower() for x in s if x.isalnum()]
        return l == l[::-1]