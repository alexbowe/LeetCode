class WordDictionary:

    def __init__(self):
        self._root = collections.defaultdict(WordDictionary)

    def addWord(self, word: str) -> None:
        if not word: self._root["$"]; return
        self._root[word[0]].addWord(word[1:])

    def search(self, word: str) -> bool:
        if not word: return "$" in self._root
        if word[0] == ".": return any(node.search(word[1:]) for node in self._root.values())
        return word[0] in self._root and self._root[word[0]].search(word[1:])
            

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)