class Solution:

    def __init__(self, w: List[int]):
        self._w = list(itertools.accumulate(w))

    def pickIndex(self) -> int:
        r = random.randint(1, self._w[-1])
        return bisect.bisect_left(self._w, r)


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()