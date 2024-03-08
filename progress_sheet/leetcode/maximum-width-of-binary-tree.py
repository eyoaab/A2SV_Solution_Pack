class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        max_width = 0
        queue = deque([(root, 0)])  
        
        while queue:
           
            cur_width = queue[-1][1] - queue[0][1] + 1
            max_width = max(max_width, cur_width)
            
          
            next_level = deque()
            for node, pos in queue:
                if node.left:
                    next_level.append((node.left, pos * 2))
                if node.right:
                    next_level.append((node.right, pos * 2 + 1))
            queue = next_level
        
        return max_width