from collections import defaultdict

TreeNode = lambda: defaultdict(TreeNode)

class Trie:

    def __init__(self):
        self._root = TreeNode()

    def insert(self, word: str) -> None:
        node = self._root
        for c in word:
            node = node[c]
        node["$"]

    def search(self, word: str) -> bool:
        return self.startsWith(word+"$")

    def startsWith(self, prefix: str) -> bool:
        node = self._root
        for c in prefix:
            if c not in node: return False
            node = node[c]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)