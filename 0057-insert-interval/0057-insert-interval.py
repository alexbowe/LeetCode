class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        def overlap(x,y):
            return y[0] <= x[1]

        def merge(x, y):
            if not overlap(x,y): return [x,y]
            return [[min(x[0],y[0]), max(x[1],y[1])]]

        def reducer(xs, y):
            if not xs: return [y]
            return xs + merge(xs.pop(),y)
        
        bisect.insort(intervals, newInterval, key=tuple)

        return reduce(reducer, intervals, [])
