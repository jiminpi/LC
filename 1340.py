class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        nums = [-1] * len(arr)
        ans = 1
        def dfs_(idx):
            if nums[idx] != -1:
                return nums[idx]
            cur = 1
            i = 1
            while i <= d and idx+i <len(arr) and arr[idx] > arr[idx+i]:
                cur = max(cur, 1 + dfs_(idx+i))
                i += 1
            i = 1
            while i <= d and idx-i >=0 and arr[idx] > arr[idx-i]:
                cur = max(cur, 1 + dfs_(idx-i))
                i += 1
            nums[idx] = cur
            return nums[idx]
        
        for i in range(len(arr)):
            ans = max(ans, dfs_(i))
        return ans
