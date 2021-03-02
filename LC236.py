# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root.val == p or root.val == q:
            return root
        
        ancestor_p = []
        ancestor_q = []
        def Search_(root, target, ancestor):
            if not root:
                return False
            if root.val == target:
                ancestor.append(root)
                return True
            
            if Search_(root.left, target, ancestor) or Search_(root.right, target, ancestor):
                ancestor.append(root)
                return True
            else:
                return False
        Search_(root, p.val, ancestor_p)
        Search_(root, q.val, ancestor_q)
        p1 = len(ancestor_p) - 1
        p2 = len(ancestor_q) - 1
        while p1 >= 0 and p2>=0 and ancestor_p[p1] == ancestor_q[p2]:
            p1 -= 1
            p2 -= 1
        return ancestor_p[p1+1]
