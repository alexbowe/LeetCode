class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict) - {""}
        stack = [s]
        seen = set()
        while stack:
            curr = stack.pop()
            if curr == "": return True
            for w in words:
                if not curr.startswith(w): continue
                new_word = curr[len(w):]
                if new_word in seen: continue
                seen.add(new_word)
                stack.append(new_word)
        return False