class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0
        maxnext, end, step = 0,0,0
        for i in range(len(nums)-1):
            maxnext = max(maxnext, i + nums[i])
            if i == end:
                end = maxnext
                step += 1
                if end >= len(nums) -1:
                    return step
            
        
