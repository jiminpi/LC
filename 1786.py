class Solution:
    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:
        g = collections.defaultdict(list)
        for u, v, w in edges:
            g[u].append((v, w))
            g[v].append((u, w))
                
        K = n
        pq = [(0, K)]
        dist = {}
        ans = {K:1}
        while pq:
            d, node = heapq.heappop(pq)
            if node in dist: continue
            dist[node] = d
            if node != K:
                ans[node] = 0
            for nei, d2 in g[node]:
                if nei not in dist:
                    heapq.heappush(pq, (d+d2, nei))
                elif dist[nei] < d:
                    ans[node] += ans[nei]
            ans[node] = ans[node]%(10**9 + 7)
            if node == 1:
                break
        return ans[1]
