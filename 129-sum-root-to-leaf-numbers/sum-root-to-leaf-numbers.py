# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        ans = 0

        def traverese(node,prev):
            nonlocal ans
            if node is None:
                return 

            prev *= 10
            prev += node.val

            if node.left is None and node.right is None:
                ans += prev

            traverese(node.left,prev)
            traverese(node.right,prev)  

        traverese(root,0)      

        return ans    



        