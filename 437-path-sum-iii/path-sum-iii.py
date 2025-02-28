# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        answer = 0

        prefix_sum = [0]
        def dfs(node,prefix_sum):
            nonlocal answer
            if not node:
                return
            prefix_sum.append(node.val + prefix_sum[-1])
            
            n = len(prefix_sum)
            final = prefix_sum[-1]
           
            for i in range(n-1):
                if final - prefix_sum[i] == targetSum:
                    answer += 1
            
            #print(prefix_sum)
            dfs(node.left,prefix_sum)
            dfs(node.right,prefix_sum)
            prefix_sum.pop()
        
        dfs(root,prefix_sum)                                 
        return answer