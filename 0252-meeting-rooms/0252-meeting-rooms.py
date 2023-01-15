class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key=tuple)
        
        overlap = lambda a,b: b[0]<a[1]
        
        def pairs(xs):
            a,b = itertools.tee(xs)
            next(b,None)
            return zip(a,b)
        
        return not any(overlap(a,b) for a,b in pairs(intervals))