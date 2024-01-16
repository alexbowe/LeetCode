class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        seen = {""}
        prefixes = {""}

        while prefixes:
            if s in prefixes: return True
            prefixes = {
                p + w
                for p in prefixes
                for w in wordDict
                if s.startswith(p + w)
                and p + w not in seen
            }
            seen |= prefixes

        return False
