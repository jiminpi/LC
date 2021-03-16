class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        intervals.sort(key=lambda x: x[1])
        n = len(intervals)
        cur_end = intervals[0][1]
        count = 1
        for start, end in intervals[1:]:
            if start >= cur_end:
                count += 1
                cur_end = end
        return n - count
