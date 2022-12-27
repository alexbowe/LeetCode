class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def new_words(w):
            alphabet = "abcdefghijklmnopqrstuvwxyz"
            return {w[:i] + c + w[i+1:] for i in range(len(w)) for c in alphabet}
        
        words = set(wordList) - {""}
        
        level = {beginWord}
        n = 0
        while level:
            n+=1
            if endWord in level: return n
            level = {nw for w in level for nw in new_words(w) if nw in words}
            words -= level
        return 0