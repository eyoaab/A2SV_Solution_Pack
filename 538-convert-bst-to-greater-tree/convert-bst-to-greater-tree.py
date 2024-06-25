class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
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