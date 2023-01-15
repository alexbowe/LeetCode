from heapq import heappush, heappushpop

class MedianFinder:

    def __init__(self):
        self._stacks = [], []

    def addNum(self, num: int) -> None:
        small, large = self._stacks
        if len(small) < len(large): heappush(small, -heappushpop(large, num))
        else                      : heappush(large, -heappushpop(small, -num))

    def findMedian(self) -> float:
        small, large = self._stacks
        if len(small) < len(large): return large[0]
        return (large[0]-small[0])/2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()