# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans=[]
        def helper(node,answer):
            if node is None:
                return 
            helper(node.left,answer)
            answer.append(node.val)
            helper(node.right,answer)

        helper(root,ans)
        return ans[k-1]  

       
    
            
            
