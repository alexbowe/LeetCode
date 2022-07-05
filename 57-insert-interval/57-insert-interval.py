from bisect import bisect_left

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        insert_location = bisect_left(intervals, tuple(newInterval), key=lambda x: tuple(x))
        
        result = intervals[:insert_location]
        intervals = [newInterval] + intervals[insert_location:]
        
        def overlap(a,b):
            return b[0] <= a[1]
        
        def merge(a,b):
            if overlap(a,b): return [[min(a[0], b[0]), max(a[1], b[1])]]
            return [a,b]
        
        for curr in intervals:
            if not result:
                result.append(curr)
                continue
            
            prev = result.pop()
            result.extend(merge(prev, curr))
        
        return result