class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=tuple)
        
        def overlaps(a, b):
            return b[0] <= a[1]
        
        def merge_intervals(a, b):
            if not overlaps(a,b):
                return [a, b]
            
            return [[min(a[0], b[0]), max(a[1],b[1])]]
        
        def reducer(xs, x):
            if not xs: return [x]
            prev = xs.pop()
            return xs + merge_intervals(prev, x)
                
        return reduce(reducer, intervals, [])
        