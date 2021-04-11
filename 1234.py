class Solution:
    def balancedString(self, s: str) -> int:
        count = defaultdict(int)
        for s_ in s:
            count[s_] += 1
        n = len(s)
        if count['Q'] == n/4 and count['W'] == n/4 and count['E'] == n/4 and count['R'] == n/4:
            return 0 
        l , r = 0, 0
        ans = n
        for r in range(n):
            count[s[r]] -= 1
            while l <= r and count['Q'] <= n/4 and count['W'] <= n/4 and count['E'] <= n/4 and count['R'] <= n/4:
                ans = min(ans, r-l+1)
                count[s[l]] += 1
                l += 1
        return ans
