# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        referance=defaultdict(list)

        def helper(node,row,col):
            if not node:
                return 
           
            helper(node.left,row+1,col-1) 
            referance[row].append([col,node.val])
            helper(node.right,row+1,col+1) 

        helper(root,0,0) 
        answer=[]
        
        ref=sorted(referance.keys())
        for key in ref:
            val=referance[key]
            #print(key,val)
            temp=[]
            for k,v in val:
                temp.append(v)
                
            if key%2==0:
                answer.append(temp)
            else:
                answer.append(temp[::-1])       
    
        return answer    
        