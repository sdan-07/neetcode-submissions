# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(root):


            inorderNodes=[]

            inorder(inorderNodes, root)
            n=len(inorderNodes)

            # check if sorted
            for i in range(n-1):
                if inorderNodes[i] >= inorderNodes[i+1]:
                    return False

            return True

        def inorder(inorderNodes, root):
            if not root: return

            inorder(inorderNodes, root.left)
            inorderNodes.append(root.val)
            inorder(inorderNodes, root.right)

        return valid(root)