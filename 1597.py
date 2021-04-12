# Definition for a binary tree node.
# class Node(object):
#     def __init__(self, val=" ", left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def expTree(self, s: str) -> 'Node':
        #https://zhuanlan.zhihu.com/p/54670963 
        ops = {'+':1, '-': 1, '*':2, '/':2}
        ops_stk = []
        node_stk = []
        for c in s:
            if c.isdigit():
                node_stk.append(Node(c))
            elif c == '(':
                ops_stk.append(c)
            elif c == ')':
                while ops_stk and ops_stk[-1] != '(':
                    right = node_stk.pop()
                    left = node_stk.pop()
                    cur = Node(ops_stk.pop(), left, right)
                    node_stk.append(cur)
                ops_stk.pop()
            else:
                while ops_stk and ops_stk[-1]!='(' and ops[ops_stk[-1]] >= ops[c]:
                    right = node_stk.pop()
                    left = node_stk.pop()
                    cur = Node(ops_stk.pop(), left, right)
                    node_stk.append(cur)
                ops_stk.append(c)
        while ops_stk:
            right = node_stk.pop()
            left = node_stk.pop()
            cur = Node(ops_stk.pop(), left, right)
            node_stk.append(cur)
        return node_stk[0]
