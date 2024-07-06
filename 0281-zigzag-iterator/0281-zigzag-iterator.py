import itertools as it

def zip(xs, ys):
    i, j = 0, 0
    while i<len(xs) and j<len(ys):
        yield xs[i]
        yield ys[j]
        i+=1; j+=1
    
    while i<len(xs):
        yield xs[i]
        i+=1
    
    while j<len(ys):
        yield ys[j]
        j+=1


class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self._it = zip(v1,v2)
        self._next = next(self._it, None)

    def next(self) -> int:
        x, self._next = self._next, next(self._it, None)
        return x

    def hasNext(self) -> bool:
        return self._next is not None

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())