class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        for group in zip(*strs):
            if not all(x == group[0] for x in group): break
            prefix += group[0]
        return prefix