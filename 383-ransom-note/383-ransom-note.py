class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        return not bool(collections.Counter(ransomNote) - collections.Counter(magazine))