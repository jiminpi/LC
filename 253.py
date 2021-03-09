class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # M1: Heap
        intervals.sort()
        hp = [intervals[0][1]]
        heapq.heapify(hp)
        for interval in intervals[1:]:
            if hp and interval[0] >= hp[0]:
                heapq.heappop(hp)
                
            heapq.heappush(hp, interval[1])
        return len(hp)
