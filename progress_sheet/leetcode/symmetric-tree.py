# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def check(self,node1,node2):
        if (not node1) and  (not node2):#
            return True
        if (not node1) or (not node2):
            return False

        if node1.val!=node2.val:
            return False
       
        return self.check(node1.left,node2.right) and self.check(node1.right,node2.left)  
              
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.check(root.left,root.right) 


        