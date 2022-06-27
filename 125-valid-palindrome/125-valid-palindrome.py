class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphabet = set("abcdefghijklmnopqrstuvwxyz0123456789")
        def filter_non_alpha(s):
            for x in s:
                if x.lower() in alphabet:
                    yield x.lower()
        s = "".join(filter_non_alpha(s))
        return s == s[::-1]