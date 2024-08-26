"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        answer = []

        def traverse(node):

            if node is None:
                return 


            for neg in node.children:
                traverse(neg)

            answer.append(node.val)  

        traverse(root)  
        return answer    