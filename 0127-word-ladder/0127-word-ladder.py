class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def new_word(w):
            alphabet = "abcdefghijklmnopqrstuvwxyz"
            return [w[:i]+c+w[i+1:] for c in alphabet for i in range(len(w))]
        words = set(wordList)
        n = 0
        q = {beginWord}
        while q:
            n+=1
            if endWord in q: return n
            q = {nw for w in q for nw in new_word(w) if nw in words}
            words.difference_update(q)
        return 0