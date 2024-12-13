# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1 is None and root2 is None:
            return None

        value1 = root1.val if root1 else 0
        value2 = root2.val if root2 else 0

        sum_ =  value1 + value2 

        mergedNode =  TreeNode(sum_)

        mergedNode.left = self.mergeTrees(root1.left if root1 else None ,root2.left if root2 else None)
        mergedNode.right = self.mergeTrees(root1.right if root1 else None ,root2.right if root2 else None) 

        return mergedNode
        