class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def new_words(w):
            alphabet = "abcdefghijklmnopqrstuvwxyz"
            return [w[:i] + c + w[i+1:] for c in alphabet for i in range(len(w))]
        
        words = set(wordList)
        level = {beginWord}
        n = 0
        while level:
            n += 1
            if endWord in level: return n
            level = {x for w in level for x in new_words(w) if x in words}
            words.difference_update(level)
        return 0