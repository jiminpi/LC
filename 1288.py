class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        if n <= 1:
            return 0
        intervals.sort()
        ans = 0
        prev = intervals[0]
        for start, end in intervals[1:]:
            if start == prev[0]:
                ans += 1
                prev = [start, end]
            elif end <= prev[1]:
                ans += 1
            else:
                prev = [start, end]
        return n - ans
                
