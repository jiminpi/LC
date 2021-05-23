class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        left = 1
        if hour > int(hour):
            right = max(max(dist[:-1]), dist[-1]//(hour-int(hour))+1)
        else:
            right = max(dist)
        if hour <= len(dist)-1:
            return -1 
        
        def helper_(speed):
            time = 0
            for d in dist[:-1]:
                time += (d + speed - 1) // speed
            time += dist[-1]/speed
            return time
        
        while left + 1 < right:
            mid = left + (right - left)//2
            time = helper_(mid)
            if time == hour:
                return int(mid)
            elif time < hour:
                right = mid
            else:
                left = mid
        
        time = helper_(left)
        if time <= hour:
            return int(left)
        else:
            return int(right)
