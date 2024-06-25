# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
      
        self.sum = 0
        
        def dfs(node):
            if not node:
                return
            if node.right:
                dfs(node.right)
            self.sum += node.val
            node.val = self.sum
            if node.left:
                dfs(node.left)
        
        dfs(root)
        return root