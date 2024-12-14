# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:

        self.ans = 0

        def postOrder(node):
            if not node:
                return 0,float('inf'),float('-inf')

            leftSum ,leftMin , leftMax = postOrder(node.left) 
            rightSum ,rightMin , rightMax  = postOrder(node.right)

            if leftMax < node.val < rightMin:
                currentSum = leftSum + rightSum + node.val
                self.ans = max(self.ans , currentSum)

                return currentSum , min(node.val,leftMin) , max(node.val,rightMax)

            else:
                return 0, float('-inf') , float('inf')

        postOrder(root)

        return self.ans            
        