class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        minval, maxval, n = min(nums), max(nums), len(nums)
        gap = max((maxval - minval + n - 2) //(n-1), 1)
        if gap == 0:
            return 0
        b_min = [None] * (n+1)
        b_max = [None] * (n+1)
        for val in nums:
            b_idx = (val-minval)//gap
            if b_min[b_idx]:
                b_min[b_idx] = min(b_min[b_idx], val)
                b_max[b_idx] = max(b_max[b_idx], val)
            else:
                b_min[b_idx] = val
                b_max[b_idx] = val
                
        last = minval
        ans = 0
        for i in range(n):
            if b_min[i]:
                ans = max(ans, b_max[i]-b_min[i])
                ans = max(ans, b_min[i] - last)
                last = b_max[i]
        return ans
