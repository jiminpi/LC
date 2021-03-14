class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # if not intervals or not newInterval:
        #     return intervals + newInterval
        l = []
        r = []
        start, end = newInterval
        for interval in intervals:
            if interval[1] < start:
                l.append(interval)
            elif interval[0] > end:
                r.append(interval)
            else:
                start = min(start, interval[0])
                end = max(end, interval[1])
        return l + [[start, end]] +r
