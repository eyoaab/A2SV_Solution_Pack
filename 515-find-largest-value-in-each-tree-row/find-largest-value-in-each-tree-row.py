# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        answer=[]
        queue=deque([root])

        while queue:
            next_level=[]
            cur_max=float('-inf')
            for q in  queue:
                if q:
                    cur_max=max(cur_max,q.val)
                    next_level.append(q.left)
                    next_level.append(q.right)
            queue=next_level
            if cur_max!=float('-inf'):
                answer.append(cur_max) 

        return answer                  