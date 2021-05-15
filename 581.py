class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        # Best: O(n), O(1)
        curmin, curmax = float('inf'), float('-inf')
        local_appear = False
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                local_appear = True
                curmin = min(curmin, nums[i])
        
        if not local_appear:
            return 0
        
        for i in range(len(nums)-2, -1, -1):
            if nums[i+1] < nums[i]:
                curmax = max(curmax, nums[i])

        for l in range(len(nums)):
            if nums[l] > curmin:
                break
        for r in range(len(nums)-1, -1, -1):
            if nums[r] < curmax:
                break
        return r-l+1
    
# class Solution:
#     def findUnsortedSubarray(self, nums: List[int]) -> int:
#         # time: O(n), space O(n)
#         stack = []
#         curmin = len(nums)
#         for i in range(len(nums)):
#             while stack and nums[stack[-1]] > nums[i]:
#                 curmin = min(stack.pop(), curmin)
#             stack.append(i)
#         if curmin == len(nums):
#             return 0
#         curmax = 0
#         stack = []
#         for i in range(len(nums)-1, -1, -1):
#             while stack and nums[stack[-1]] < nums[i]:
#                 curmax = max(curmax, stack.pop())
#             stack.append(i)

#         return curmax - curmin + 1
    
# class Solution:
#     def findUnsortedSubarray(self, nums: List[int]) -> int:
#         #time O(nlogn), space O(n)
#         nums_sorted = sorted(nums)
#         l,r = None, None
#         for i in range(len(nums)):
#             if nums_sorted[i] != nums[i]:
#                 l = i
#                 break
#         if l is None:
#             return 0
#         for i in range(len(nums)-1, -1, -1):
#             if nums_sorted[i] != nums[i]:
#                 r = i
#                 break
#         return r-l+1
