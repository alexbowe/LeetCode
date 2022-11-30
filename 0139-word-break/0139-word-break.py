class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if not s: return True
        
        words = sorted(wordDict, key=lambda x: -len(x))
        seen = set()
        stack = [s]
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