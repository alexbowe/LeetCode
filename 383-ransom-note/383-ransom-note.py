class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        from collections import Counter
        return not bool(Counter(ransomNote) - Counter(magazine))