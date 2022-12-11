class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict) - {""}
        seen = set()
        level = [s]
        while level:
            curr = level.pop()
            if curr == "": return True
            for w in words:
                if curr.startswith(w):
                    new_word = curr[len(w):]
                    if new_word in seen: continue
                    seen.add(new_word)
                    level.append(new_word)
        return False