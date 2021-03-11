class MyCalendarThree:

    def __init__(self):
        self.delta = collections.defaultdict(int)
        

    def book(self, start: int, end: int) -> int:
        self.delta[start] += 1
        self.delta[end] -= 1
        
        ans = 0
        active = 0
        for t in sorted(self.delta):
            active += self.delta[t]
            ans = max(ans, active)
        return ans      
