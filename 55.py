class Solution:
    def canJump(self, nums: List[int]) -> bool:
        target = len(nums) - 1
        max_cur = 0
        for i in range(len(nums)):
            if max_cur < i:
                return False
            max_cur = max(max_cur, i + nums[i])
            if max_cur >= target:
                return True
        
        
