import functools
def comparator(s1, s2):
    if int(s1+s2) < int(s2+s1):
        return -1
    if int(s1+s2) > int(s2+s1):
        return 1
    return 0

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = [str(num) for num in nums]

        nums_sorted = sorted(nums, key = functools.cmp_to_key(comparator),  reverse = True)
        if nums_sorted[0] == '0':
            return '0'
        else:
            return ''.join(nums_sorted)
