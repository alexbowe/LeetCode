class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        seen = {s}
        q = [s]
        
        while q:
            curr = q.pop()
            if curr == "": return True
            for w in wordDict:
                if not curr.startswith(w): continue
                new_word = curr[len(w):]
                if new_word in seen: continue
                q.append(new_word)
                seen.add(new_word)
        return False