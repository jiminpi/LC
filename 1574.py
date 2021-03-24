class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        i, j = 0, len(arr)-1
        while j > 0 and arr[j-1] <= arr[j]:
            j -= 1
        if not j:
            return 0
        
        ans = j
        for i in range(len(arr)-1):
            if i > 0 and arr[i] < arr[i-1]:
                break
            while j < len(arr) and arr[j] < arr[i]:
                j += 1
            ans = min(ans, j - 1 - (i+1) +1)
        return ans
