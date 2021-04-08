# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipMatchVoyage(self, root: TreeNode, voyage: List[int]) -> List[int]:
        ans = []
        self.cur = 0
        def dfs_(root):
            if not root:
                return
            if root.val != voyage[self.cur]:
                ans.append(-1)
                return
            if self.cur < len(voyage)-1 and root.left and root.left.val != voyage[self.cur+1]:
                ans.append(root.val)
                self.cur += 1
                dfs_(root.right)
                dfs_(root.left)
            else:
                self.cur += 1
                dfs_(root.left)
                dfs_(root.right)
            return 
        dfs_(root)
        if -1 in ans:
            print(ans)
            return [-1]
        else:
            return ans
