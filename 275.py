class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        if citations[-1] == 0:
            return 0

        start, end = 0, n-1
        while start + 1 < end:
            mid = start + (end-start)//2
            if citations[mid] == n - mid:
                return n-mid
            elif citations[mid] > n - mid:
                end = mid
            else:
                start = mid
        if citations[start] >= n-start:
            return n-start
        else:
            return n-end
