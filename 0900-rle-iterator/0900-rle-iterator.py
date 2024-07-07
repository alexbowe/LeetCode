class RLEIterator:

    def __init__(self, encoding: List[int]):
        self._enc = encoding

    def next(self, n: int) -> int:
        while self._enc:
            if n <= self._enc[0]:
                self._enc[0] -= n
                return self._enc[1]
            else:
                n -= self._enc[0]
                self._enc = self._enc[2:]
        return -1
        


# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(encoding)
# param_1 = obj.next(n)