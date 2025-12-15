# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        def dfs(i):

            if not i:
                return []

            if not i.left and not i.right:
                return [i.val]
            
            return dfs(i.left) + dfs(i.right)

        seq1 = dfs(root1)
        seq2 = dfs(root2)

        return seq1==seq2