# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        self.i = 0
        return self.preorder_(S, 0)
    def preorder_(self, S, d):
        nextD = self.getDepth_(S)
        if nextD != d:
            self.i -= nextD
            return None
        root = TreeNode(self.getValue_(S))
        root.left = self.preorder_(S, d+1)
        root.right = self.preorder_(S, d+1)
        return root
    def getValue_(self, S):
        val = 0
        while self.i < len(S) and S[self.i] != '-':
            val = val*10 + ord(S[self.i])-ord('0')
            self.i += 1
        return val
    def getDepth_(self, S):
        depth = 0
        while self.i < len(S) and S[self.i] == '-':
            depth+= 1
            self.i+= 1
        return depth
