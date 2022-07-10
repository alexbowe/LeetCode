from collections import defaultdict
def tree_node(): return defaultdict(tree_node)

TERMINAL = "$"

class Trie:
    def __init__(self):
        self._root = tree_node()
        self._root["$"]

    def insert(self, word: str) -> None:
        curr = self._root
        for x in word + TERMINAL:
            curr = curr[x]

    def search(self, word: str) -> bool:
        return self.startsWith(word+TERMINAL)

    def startsWith(self, prefix: str) -> bool:
        curr = self._root
        for x in prefix:
            if x not in curr: return False
            curr = curr[x]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)