# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        ref=defaultdict(int)
        def help(node):
            if node:
                ref[node.val]+=1
                help(node.left)
                help(node.right)
            else:
                return    
                
        help(root)
        ma=max(ref.values())
        answer=[]
        for i,j in ref.items():
            if j==ma:
                answer.append(i)
        return answer          
        