# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:

        ans = 0

        def postOrder(node):
            nonlocal ans
            if node is None:
                return 0, float('inf'), float('-inf')

            leftSum, leftMin, leftMax =  postOrder(node.left)
            rightSum, rightMin, rightMax =  postOrder(node.right)  

            if leftMax < node.val < rightMin:
                
                currentSum = node.val + leftSum + rightSum
                ans = max(ans,currentSum)
                return currentSum,min(node.val,leftMin),max(node.val,rightMax)

            else:
                return 0, float('-inf'), float('inf')

        postOrder(root)
        return ans        



        