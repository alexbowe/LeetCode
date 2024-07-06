def flatten(xs):
    for row in xs:
        yield from row

class Vector2D:

    def __init__(self, vec: List[List[int]]):
        self._it = flatten(vec)
        self._next = next(self._it, None)

    def next(self) -> int:
        x, self._next = self._next, next(self._it, None)
        return x

    def hasNext(self) -> bool:
        return self._next is not None
        


# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(vec)
# param_1 = obj.next()
# param_2 = obj.hasNext()