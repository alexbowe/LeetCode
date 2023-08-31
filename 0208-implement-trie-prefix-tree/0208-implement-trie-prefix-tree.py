class Trie:

    def __init__(self):
        self._root = collections.defaultdict(Trie)

    def insert(self, word: str) -> None:
        if not word: self._root["$"]
        else: self._root[word[0]].insert(word[1:])

    def search(self, word: str) -> bool:
        return self.startsWith(word+"$")

    def startsWith(self, prefix: str) -> bool:
        if not prefix: return True
        return prefix[0] in self._root and self._root[prefix[0]].startsWith(prefix[1:])


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)