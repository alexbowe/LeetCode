class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        def overlaps(a,b):
            return b[0]<=a[1]
        
        def merge(a,b):
            if overlaps(a,b): return [[min(a[0],b[0]), max(a[1],b[1])]]
            return [a,b]
        
        def reducer(xs, x):
            if not xs: return [x]
            prev = xs.pop()
            return xs + merge(prev,x)
        
        i = bisect.bisect_left(intervals, tuple(newInterval), key=tuple)
        intervals.insert(i, newInterval)
        return reduce(reducer, intervals, [])
            