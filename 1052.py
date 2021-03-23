class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        base = 0
        best_window = 0
        cur_window = 0
        for i in range(len(customers)):
            if not grumpy[i]:
                base += customers[i]
            else:
                cur_window += customers[i]
            if i >= X and grumpy[i-X]:
                cur_window -= customers[i-X]            
            best_window = max(best_window, cur_window)
        return base + best_window
                
