def decode(s):
    count = 0
    char = ""
    for x in s:
        if x.isdigit():
            count = 10 * count + int(x)
        else:
            for _ in range(count): yield char
            count = 0
            char = x
    for _ in range(count): yield char

class StringIterator:

    def __init__(self, compressedString: str):
        self._it = decode(compressedString)
        self._next = next(self._it, None)

    def next(self) -> str:
        if not self.hasNext(): return " "
        x, self._next = self._next, next(self._it, None)
        return x

    def hasNext(self) -> bool:
        return self._next is not None
        


# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()