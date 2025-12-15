# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
 # Map to store number of times each prefix sum has occurred
        prefix = defaultdict(int)
        prefix[0] = 1 

        def dfs(node, curr_sum):
            if node is None:
                return 0
            
            curr_sum += node.val
            count = prefix[curr_sum - targetSum]
            
            prefix[curr_sum] += 1
            
            count += dfs(node.left, curr_sum)
            count += dfs(node.right, curr_sum)
            
            prefix[curr_sum] -= 1
            
            return count
        
        return dfs(root, 0)

#         if root is None:
#             return 0
        
#         def countPaths(node,targetSum):
#             count = 0
            
#             if node is None:
#                 return 0
            
#             if node.val == targetSum:
#                 count += 1
            
#             count += countPaths(node.left,targetSum - node.val)
#             count += countPaths(node.right,targetSum-node.val)

#             return count

        
#         return countPaths(root,targetSum) + self.pathSum(root.left,targetSum) + self.pathSum(root.right,targetSum)

