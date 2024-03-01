# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        self.answer=0
        self.helper(root,root.val,root.val)
        return self.answer 

    def helper(self,node,min_val,max_val):
        if  node is None:
            return 0
        self.answer=max(self.answer,max(abs(min_val-node.val),abs(max_val-node.val)))
        max_val=max(max_val,node.val)  
        min_val=min(min_val,node.val) 

        self.helper(node.left,min_val,max_val)
        self.helper(node.right,min_val,max_val)             