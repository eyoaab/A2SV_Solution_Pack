# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        delete =  set(to_delete)
        answer = set()
        answer.add(root)

        def dfs(node):
            if not node:
                return
            if node.val in delete:
                if node.left:
                    answer.add(node.left) 
                if node.right:
                    answer.add(node.right)

            dfs(node.left)
            dfs(node.right)

            if node.left and node.left.val in delete:
                node.left = None  
            if node.right and node.right.val in delete:
                node.right = None
        dfs(root)
        return [node for node in answer if node.val not in delete]



        