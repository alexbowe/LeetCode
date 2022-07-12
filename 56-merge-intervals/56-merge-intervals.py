class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=tuple)
        
        def overlaps(a,b):
            return b[0]<=a[1]
        
        def merge(a,b):
            return [[min(a[0],b[0]), max(a[1],b[1])]] if overlaps(a,b) else [a,b]
        
        def reducer(xs, x):
            if not xs: return [x]
            prev = xs.pop()
            xs.extend(merge(prev, x))
            return xs
        
        return reduce(reducer, intervals, [])