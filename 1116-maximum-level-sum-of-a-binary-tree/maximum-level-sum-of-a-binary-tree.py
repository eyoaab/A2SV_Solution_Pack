# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        queue = deque([root])
        heap = []
        level = 1
        

        heappush(heap,[- root.val,level])

        while queue:
            level += 1

            length = len(queue)

            levelSum = 0
            isVisited = False

            for _ in range(length):
                node = queue.popleft()

                if node.left:
                    levelSum -=  node.left.val
                    queue.append(node.left)
                    isVisited  = True

                if node.right:
                    levelSum -=  node.right.val
                    queue.append(node.right)
                    isVisited  = True


            if isVisited:
                heappush(heap,[levelSum,level])        

       

        return heappop(heap)[-1]             