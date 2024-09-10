class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: 
            return node
        
        queue, clones = deque([node]), {node.val: Node(node.val, [])}
        
        while queue:
            current = queue.popleft() 
            current_clone = clones[current.val]            

            for child in current.neighbors:
                if child.val not in clones:
                    clones[child.val] = Node(child.val, [])
                    queue.append(child)
                    
                current_clone.neighbors.append(clones[child.val])
                
        return clones[node.val]