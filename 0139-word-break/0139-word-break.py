class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = sorted(wordDict, key=lambda x: -len(x))
        stack = [s]
        seen = set()
        while stack:
            curr = stack.pop()
            if curr == "": return True
            for word in words:
                if curr.startswith(word):
                    new_word = curr[len(word):]
                    if new_word in seen: continue
                    seen.add(new_word)
                    stack.append(new_word)
        return False