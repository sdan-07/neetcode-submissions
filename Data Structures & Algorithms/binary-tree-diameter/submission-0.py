# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        longest = 0

        def dfs(root):
            nonlocal longest

            if not root: return 0

            lpath = dfs(root.left)
            rpath = dfs(root.right)

            diameter = lpath+rpath

            longest = max(longest, diameter)

            return 1+max(lpath,rpath)

        dfs(root)
        return longest