def combinations(opts, k):
    def helper(part, opts, k):
        if k == 0: yield part; return
        for i in range(len(opts)):
            yield from helper(part+[opts[i]], opts[i+1:], k-1)
    return helper([], opts, k)

class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self._it = ("".join(com) for com in combinations(characters, combinationLength))
        self._next = next(self._it, None)

    def next(self) -> str:
        x, self._next = self._next, next(self._it, None)
        return x

    def hasNext(self) -> bool:
        return self._next is not None

# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()