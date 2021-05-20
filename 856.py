class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        def helper_(l_sub, r_sub):
            if r_sub - l_sub == 1:
                return 1
            count = 0
            for i in range(l_sub, r_sub):
                if s[i] == '(':
                    count += 1
                elif s[i] == ')':
                    count -= 1
                if count == 0:
                    return helper_(l_sub, i) + helper_(i+1, r_sub)
                
            return 2*helper_(l_sub+1, r_sub-1)
        
        return helper_(0, len(s)-1)
