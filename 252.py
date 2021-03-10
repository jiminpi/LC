class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:  
        if not intervals:
            return True
        intervals.sort(key= lambda x:x[0])
        last_end = intervals[0][1]
        for start, end in intervals[1:]:
            if start < last_end:
                return False
            last_end = end
        return True
