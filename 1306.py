class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        visited = [False] * len(arr)
        def dfs_(idx):
            if idx >= len(arr) or idx < 0 or visited[idx]:
                return False
            if arr[idx] == 0:
                return True
            visited[idx] = True
            if dfs_(idx + arr[idx]) or dfs_(idx - arr[idx]):
                return True
            else:
                return False
            
        return dfs_(start)
            
