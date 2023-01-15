class Solution:

    def __init__(self, w: List[int]):
        self._prefix_sum = reduce(lambda xs,x: xs+[xs[-1]+x], w, [0])
        self._prefix_sum = [s/self._prefix_sum[-1] for s in self._prefix_sum]
        print(self._prefix_sum)

    def pickIndex(self) -> int:
        r = random.random()
        return bisect.bisect_left(self._prefix_sum, r)-1


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()