# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.answer=0
        def solve(node):
            if not node:
                return
            if node.val<=high and node.val>=low:
                self.answer+=node.val 
            solve(node.left)
            solve(node.right)

        solve(root)
        return self.answer               

        