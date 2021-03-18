class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if len(points) <= 1:
            return len(points)
        points.sort(key=lambda x:x[1])
        ans = 1
        prev = points[0][1]
        for start, end in points[1:]:
            if start > prev:
                ans+=1
                prev = end
        return ans
