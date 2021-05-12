class Solution:
    def oddEvenJumps(self, arr: List[int]) -> int:
        N = len(arr)
        firstSmaller = [-1] * N
        firstLarger =  [-1] * N
        
        def helper_(idx_sorted):
            ans = [-1] * N
            stack = []
            for i in idx_sorted:
                while stack and stack[-1] < i:
                    ans[stack.pop()] = i
                stack.append(i)
            return ans
        
        
        id_ascending = list(range(N))
        id_ascending.sort(key = lambda i: arr[i])
        id_descending = list(range(N))
        id_descending.sort(key = lambda i: -arr[i])
        firstLarger = helper_(id_ascending)
        firstSmaller = helper_(id_descending)


        
        dp_odd, dp_even = [False]*N, [False]*N
        dp_odd[-1] = dp_even[-1] = True
        for i in range(N-2, -1, -1):
            if firstSmaller[i] != -1:
                dp_even[i] = dp_odd[firstSmaller[i]]
            if firstLarger[i] != -1:
                dp_odd[i] = dp_even[firstLarger[i]]
        return sum(dp_odd)
            
            
        
