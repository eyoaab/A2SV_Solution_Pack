"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
                return root
        queue = deque([root])
            
            # queue.append()
            
        tail = root
        while queue:
            node = queue.popleft()

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
                
            if node == tail:
                node.next = None
                tail = queue[-1] if len(queue) > 0 else None
            else:
                node.next = queue[0]
                
        return root