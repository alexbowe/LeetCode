class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        from bisect import bisect_left
        i = bisect_left(intervals, tuple(newInterval), key=tuple)
        intervals.insert(i, newInterval)
        
        def overlap(a,b):
            return b[0]<=a[1]
        
        def merge(a,b):
            if overlap(a,b):
                return [[min(a[0],b[0]),max(a[1],b[1])]]
            return [a,b]
        
        def reducer(xs, x):
            prev = xs.pop()
            return xs + merge(prev, x)
        
        return reduce(reducer, intervals[1:], [intervals[0]])