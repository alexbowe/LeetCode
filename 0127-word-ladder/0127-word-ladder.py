class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def neighbors(w):
            alpha = "abcdefghijklmnopqrstuvwxyz"
            return [
                w[:i] + c + w[i+1:]
                for c in alpha
                for i in range(len(w))
            ]
        
        words = set(wordList)
        
        n = 0
        level = set([beginWord])
        while level:
            n+=1
            if endWord in level: return n
            level = {n for w in level for n in neighbors(w) if n in words}
            words.difference_update(level)
        
        return 0