# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        prev, nxt = None, None
        first, second = None, None
        def inorder_(root):
            nonlocal prev, nxt, first, second
            if not root:
                return
            inorder_(root.left)
            if prev and prev.val > root.val:
                if not first:
                    first = prev
                second = root
            prev = root
            inorder_(root.right)
            return
        inorder_(root)
        first.val, second.val = second.val, first.val
        return
