class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        for chars in zip(*strs):
            if any(x!=chars[0] for x in chars): break
            prefix+=chars[0]
        return prefix