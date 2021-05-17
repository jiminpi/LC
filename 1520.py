class Solution:
    def maxNumOfSubstrings(self, s: str) -> List[str]:
        starts, ends = [-1]*26, [-1]*26
        s = list(s)
        
        for i, s_i in enumerate(s):
            idx = ord(s_i) - ord('a')
            if starts[idx] == -1:
                starts[idx] = i
                ends[idx] = i
            else:
                ends[idx] = i
        
        def extend_(l, r):
            p = r
            i = l
            while i <= p:
                idx = ord(s[i]) - ord('a')
                if starts[idx] < l:
                    return -1
                p = max(ends[idx], p)
                i += 1
            return p
        
        intervals = []
        visited = [False]*26
        for i, s_i in enumerate(s):
            idx = ord(s_i) - ord('a')
            if not visited[idx]:
                visited[idx] = True
                p = extend_(starts[idx], ends[idx])
                if p != -1:
                    intervals.append([starts[idx], p])
        
        intervals.sort(key = lambda x:x[1])
        last = -1
        ans = []
        for interval in intervals:
            if interval[0] > last:
                ans.append(''.join(s[interval[0]:interval[1]+1]))
                last = interval[1]
        return ans
