class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        level = {s}
        seen = {s}
        while level:
            if "" in level: return True
            level = {x[len(w):] for x in level for w in words if x.startswith(w)}
            seen.update(level)
        return False