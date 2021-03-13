class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        p1, p2, ans = 0, 0, []
        while p1< len(firstList) and p2 < len(secondList):
            start1, end1 = firstList[p1]
            start2, end2 = secondList[p2]
            if max(start1, start2) <= min(end1, end2):
                ans.append([max(start1, start2), min(end1, end2)])
            if end1 < end2:
                p1 += 1
            elif end1 > end2:
                p2 += 1
            else:
                p1+=1
                p2+=1
        return ans
