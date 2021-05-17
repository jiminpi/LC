class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks.sort(key = lambda x:x[1]-x[0], reverse = True)
        ans = 0
        cur = 0
        for interval in tasks:
            if cur < interval[1]:
                ans += interval[1] - cur
                cur = interval[1]
            cur -= interval[0]
        return ans
