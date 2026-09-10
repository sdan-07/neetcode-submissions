# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def check(p,q):
            if not p: return False
            if not q: return True

            if sameTree(p,q):
                return True

            return check(p.left, q) or check(p.right,q)

        def sameTree(p,q):
            if not p and not q: return True

            if not p or not q: return False

            if p.val == q.val:
                return sameTree(p.left, q.left) and sameTree(p.right, q.right)

        return check(root, subRoot)