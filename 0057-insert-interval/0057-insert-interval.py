class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        from bisect import insort_left
        intervals = [tuple(x) for x in intervals]
        newInterval = tuple(newInterval)
        insort_left(intervals, newInterval)
        
        def overlaps(a,b):
            return b[0] <= a[1]
        
        def merge(a,b):
            if not overlaps(a,b): return [a,b]
            return [(min(a[0],b[0]), max(a[1],b[1]))]
        
        def reducer(xs, x):
            if not xs: return [x]
            prev = xs.pop()
            return xs + merge(prev, x)
        
        return reduce(reducer, intervals, [])
            