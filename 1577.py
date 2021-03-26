class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        # [TODO:] Check again over other answers.
        counter_1 = collections.defaultdict(int)
        counter_2 = collections.defaultdict(int)
        for num in nums1:
            counter_1[num] += 1
        for num in nums2:
            counter_2[num] += 1
            
        def numTriplets_(nums1, nums2, counter_1, counter_2):
            ans = 0
            for num_1 in counter_1:
                target = num_1**2
                ans_ = 0
                for num_2 in counter_2:
                    remain = target / num_2
                    if remain in counter_2:
                        if remain == num_1:
                            ans_ += counter_2[num_2] * (counter_2[num_2] - 1)
                        else:
                            ans_ += counter_2[num_2] * counter_2[remain]
                ans += counter_1[num_1] * ans_ /2
            return ans
        return int(numTriplets_(nums1, nums2, counter_1, counter_2) + numTriplets_(nums2, nums1, counter_2, counter_1))
                    
                
