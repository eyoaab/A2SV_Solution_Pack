# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans = 0

        def inorder(node,prev):
            nonlocal ans
            if not node:
                return 
            prev *= 10
            prev +=  node.val
                


            if not node.left and not node.right:
                ans += prev

            inorder(node.left,prev)
            inorder(node.right,prev)   

        inorder(root,0)
        return ans     
                    