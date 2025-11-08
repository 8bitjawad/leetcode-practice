# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.longest = 0
        
        def maxzigzag(node,d,length):
            if node is None:
                return 0
            
            self.longest = max(self.longest,length)

            maxzigzag(node.left,'l',1 if d == 'l' else length+1)
            maxzigzag(node.right,'r',1 if d == 'r' else length+1)

                
        maxzigzag(root,'l',0)
        maxzigzag(root,'r',0)

        return self.longest

        

            

        