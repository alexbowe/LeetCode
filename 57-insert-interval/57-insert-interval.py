class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        from bisect import bisect_left
        insert_idx = bisect_left(intervals, tuple(newInterval), key=tuple)
        intervals.insert(insert_idx, newInterval)
        
        def overlap(a,b):
            return b[0]<=a[1]
        
        def merge(a,b):
            if overlap(a,b):
                return [ [min(a[0], b[0]), max(a[1], b[1])] ]
            return [a, b]
        
        def reducer(xs, x):
            return xs + merge(xs.pop(), x) if xs else [x]
        
        return reduce(reducer, intervals, [])