class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def new_words(w):
            alpha = "abcdefghijklmnopqrstuvwxyz"
            return [w[:i] + c + w[i+1:] for c in alpha for i in range(len(w))]
        
        n = 0
        words = set(wordList)
        level = set([beginWord])
        while level:
            n+=1
            if endWord in level: return n
            level = {nw for w in level for nw in new_words(w) if nw in words}
            words.difference_update(level)
        
        return 0
        