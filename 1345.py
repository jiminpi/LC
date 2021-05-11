class Solution:
    def minJumps(self, arr: List[int]) -> int:
        g = collections.defaultdict(list)
        for i in range(len(arr)):
            g[arr[i]].append(i)
        q = collections.deque()
        q.append(0)
        step = 0
        visited = [False] * len(arr)
        visited[0] = True
        while q:
            ncur = len(q)
            for i in range(ncur):
                cur = q.popleft()
                if cur == len(arr)-1:
                    return step
                neighs = g[arr[cur]]
                for neigh in neighs:
                    if not visited[neigh]:
                        q.append(neigh)
                        visited[neigh] = True
                if cur + 1 < len(arr) and not visited[cur+1]:
                    q.append(cur+1)
                    visited[cur + 1] = True
                if cur - 1 >= 0 and not visited[cur-1]:
                    q.append(cur-1)
                    visited[cur-1] = True
                del g[arr[cur]]
            step += 1
        raise ValueError('Not found')
