# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        ref=[]
        def help(node,col,row):
            if node:
                ref.append([col,row,node.val])
                help(node.left,col-1,row+1)
                help(node.right,col+1,row+1)
            else:
                return
        help(root,0,0)
        ref.sort(key=lambda x:(x[0],x[1],x[2]))
        
        ref2=defaultdict(list)
        for i,j,k in ref:
            ref2[i].append(k)
        answer=[]
        for i,j in ref2.items():
            answer.append(j)

        return list(answer)            

