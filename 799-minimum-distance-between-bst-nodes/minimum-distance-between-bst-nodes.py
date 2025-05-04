# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        store = []

        node = root

        def dfs(node):
            nonlocal store
            if not node:
                return 

            store.append(node.val) 
            if node.left:
                dfs(node.left)

            if node.right:
                dfs(node.right)

            return    

        dfs(root)

        store.sort()
        ans = float('inf')

        for i in range(1,len(store)):
            ans = min(ans,store[i] - store[i - 1])   

        if ans == float('inf'):
            return -1 

        return ans            



        