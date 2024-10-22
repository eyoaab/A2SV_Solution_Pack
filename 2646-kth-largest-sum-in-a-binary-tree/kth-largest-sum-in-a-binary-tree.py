# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        queue = deque([root])

        heap = []

        heappush(heap,- root.val)

        while queue:
            length = len(queue)

            levelSum = 0

            for _ in range(length):
                node = queue.popleft()

                if node.left:
                    levelSum -=  node.left.val
                    queue.append(node.left)

                if node.right:
                    levelSum -=  node.right.val
                    queue.append(node.right)

            if levelSum != 0:
                heappush(heap,levelSum)        

        if len(heap) < k:
            return -1

        for _ in range(k - 1):
            heappop(heap)

        return - heappop(heap)              
