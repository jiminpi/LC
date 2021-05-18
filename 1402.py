class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort(reverse = True)
        last = 0
        ans = 0
        for val in satisfaction:
            if last + val > 0:
                last += val
                ans += last
            else:
                break
        return ans
