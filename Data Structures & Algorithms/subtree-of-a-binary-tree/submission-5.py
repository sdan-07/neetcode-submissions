# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
            def checkSame(p,q):
                if not p: return False
                if not q: return True
                if isSameTree(p,q):
                    return True
                return checkSame(p.left, q) or checkSame(p.right, q)

            def isSameTree(p,q):
                if not p and not q: return True
                if not p or not q: return False
                if p.val == q.val:
                    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
                return False
            
            return checkSame(root, subRoot)