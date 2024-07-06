class Solution:

    def __init__(self, w: List[int]):
        self._weights = list(itertools.accumulate((w)))

    def pickIndex(self) -> int:
        r = random.randint(1,self._weights[-1])
        return bisect.bisect_left(self._weights, r)
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()