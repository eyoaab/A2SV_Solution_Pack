# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self,node,res):
        if node is None:
            return 
        self.helper(node.left,res)
        res.append(node.val)
        self.helper(node.right,res) 


    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        ans=[]
        self.helper(root,ans)
        print(ans)
        if len(ans)<2:
            return True
        for i in range(1,len(ans)):
            if ans[i]<=ans[i-1]:
                return False    
        return True
       
            