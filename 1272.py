class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        toL, toR = toBeRemoved
        ans = []
        for start, end in intervals:
            if toL >= end or toR <= start:
                ans.append([start, end])
            else:
                if start < toL:
                    ans.append([start, toL])
                if end > toR:
                    ans.append([toR, end])
        return ans

