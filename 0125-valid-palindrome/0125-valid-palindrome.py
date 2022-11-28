class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(x.lower() for x in s if x.isalnum())
        return s == s[::-1]