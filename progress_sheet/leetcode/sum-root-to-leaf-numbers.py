# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        answer=[]
        def help(node,val):
            if not node:
                print(val)
                return
            if not node.left and not node.right:
                answer.append(val+node.val)

            val=val+node.val 
            help(node.left,val*10)
          
            help(node.right,val*10) 
        help(root,0)

        return sum(answer)              




        