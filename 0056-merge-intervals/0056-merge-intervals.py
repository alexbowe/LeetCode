class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=tuple)
        
        def overlap(x,y):
            return y[0] <= x[1]
        
        def merge(x,y):
            if not overlap(x,y): return [x,y]
            return [[min(x[0],y[0]), max(x[1],y[1])]]
        
        def reducer(xs, y):
            if not xs: return [y]
            return xs + merge(xs.pop(), y)
        
        return reduce(reducer, intervals, [])