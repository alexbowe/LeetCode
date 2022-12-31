class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        for group in zip(*strs):
            s = set(group)
            if len(s) != 1: break
            prefix += s.pop()
        return prefix