class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])
        
        ans = []
        prev = []
        for start, end in intervals:
            if not prev:
                prev = [start, end]
            elif start >= prev[0] and start <= prev[1]:
                prev = [min(start, prev[0]), max(end, prev[1])]
            else:
                ans.append(prev[:])
                prev = [start, end]
        if prev:
            ans.append(prev[:])
        return ans
