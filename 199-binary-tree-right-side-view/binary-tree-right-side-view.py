# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
       
        answer = [] 
        def bfs(queue):
            if not queue:
                return 
            level_nodes = []
            next_level = []
            
            for node in queue:
                if node:
                    level_nodes.append(node.val)
                    if node.left:
                        next_level.append(node.left)
                    if node.right:
                        next_level.append(node.right)
                else:
                    return        
            
            answer.append(level_nodes[-1])
            queue = next_level
            bfs(queue)
        bfs([root])
        return answer

    
                
                    