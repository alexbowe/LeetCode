class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key=tuple)
        return not any(intervals[i][0]<intervals[i-1][1] for i in range(1,len(intervals)))