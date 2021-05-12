class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        dp = [0] * len(nums)
        dp[0] = nums[0]
        q = collections.deque({0})
        for i in range(1, len(nums)):
            dp[i] = nums[i] + dp[q[0]]
            while q and dp[q[-1]] <= dp[i]:
                q.pop()
            if q and i - q[0] >= k:
                q.popleft()
            q.append(i)
        return dp[-1]
                
