class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter
        return Counter(x.lower() for x in s if x.isalpha()) == Counter(x.lower() for x in t if x.isalpha())