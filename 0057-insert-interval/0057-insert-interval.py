class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        def overlap(x,y):
            return y[0] <= x[1]

        def merge(xs, y):
            if not xs: return [y]
            x = xs.pop()
            return xs + [[min(x[0],y[0]), max(x[1],y[1])]] if overlap(x,y) else xs + [x,y]
        
        bisect.insort(intervals, newInterval, key=tuple)

        return reduce(merge, intervals, [])
