class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        # M2: dfs
        if len(connections) < n - 1:
            return -1
        g = [[] for i in range(n)]
        for edge in connections:
            g[edge[0]].append(edge[1])
            g[edge[1]].append(edge[0])
        
        visited = [False] * n
        def dfs_(x):
            visited[x] = True
            for nxt in g[x]:
                if not visited[nxt]:
                    dfs_(nxt)
            return
        
        ans = -1
        for i in range(n):
            if not visited[i]:
                dfs_(i)
                ans += 1
        return ans
        
#     def makeConnected(self, n: int, connections: List[List[int]]) -> int:
#         # M1: union-find
#         if len(connections) < n - 1:
#             return -1
#         p = list(range(n))
#         def find_(x):
#             if p[x] != x:
#                 p[x] = find_(p[x])
#             return p[x]
#         for edge in connections:
#             px = find_(edge[0])
#             py = find_(edge[1])
#             p[px] = py
        
#         ans = -1
#         for i in range(n):
#             if find_(i) == i:
#                 ans += 1
#         return ans
