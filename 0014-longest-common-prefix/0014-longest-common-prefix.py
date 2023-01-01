class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        N = 0
        for group in zip(*strs):
            if not all(x == group[0] for x in group): break
            N+=1
        return strs[0][:N]