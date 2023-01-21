class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        for chars in zip(*strs):
            if any(c!=chars[0] for c in chars): return prefix
            prefix += chars[0]
        return prefix