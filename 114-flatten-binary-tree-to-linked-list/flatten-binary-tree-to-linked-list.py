# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        def dfs(node):
            if not node:
                return None
            
            left_tail = dfs(node.left)
            right_tail = dfs(node.right)

            if left_tail:
                left_tail.right = node.right 
                node.right = node.left  
                node.left = None 

            return right_tail if right_tail else left_tail if left_tail else node

        dfs(root)