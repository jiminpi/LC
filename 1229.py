class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        slots1.sort(key = lambda x:x[0])
        slots2.sort(key = lambda x:x[0])
        ans = []
        p1, n1 = 0, len(slots1)
        p2, n2 = 0, len(slots2)
        if not n1 or not n2:
            return []
        
        while p1 < n1 and p2 < n2:
            s1, e1 = slots1[p1]
            s2, e2 = slots2[p2]
            if max(s1, s2) < min(e1, e2) and min(e1, e2) - max(s1, s2) >= duration:
                return [max(s1, s2), max(s1, s2)+duration]
            if e1 < e2:
                p1 += 1
            elif e1 > e2:
                p2 += 1
            else:
                p1 += 1
                p2 += 1
        return []
