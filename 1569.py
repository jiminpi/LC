class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        def ways_(cur_set):
            if len(cur_set) <= 2:
                return 1
            l = [x for x in cur_set if x<cur_set[0]]
            r = [x for x in cur_set if x>cur_set[0]]
            return math.comb(len(r) + len(l), len(l)) * ways_(l) * ways_(r) %(10**9 + 7)
        return (ways_(nums)-1) %(10**9 + 7)
            
