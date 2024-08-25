# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        def postord(node,res):
            if node is None:
                return 
            postord(node.left,res)
            postord(node.right,res) 
            res.append(node.val)  
        
        postord(root,res)
        return res