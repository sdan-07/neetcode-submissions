# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def smallest(root, k):
            nodes=[]
            inorder(root, nodes)

            return nodes[k-1]

        def inorder(root, nodes):
            if root:
                inorder(root.left,nodes)
                nodes.append(root.val)
                inorder(root.right,nodes)
        return smallest(root,k)
