from heapq import heappush, heappushpop

class MedianFinder:

    def __init__(self):
        self._heaps = [], []

    def addNum(self, num: int) -> None:
        small, large = self._heaps
        if len(large) <= len(small): heappush(large, -heappushpop(small, -num))
        else                       : heappush(small, -heappushpop(large,  num))

    def findMedian(self) -> float:
        small, large = self._heaps
        if len(large) > len(small): return float(large[0])
        return (large[0] - small[0])/2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()