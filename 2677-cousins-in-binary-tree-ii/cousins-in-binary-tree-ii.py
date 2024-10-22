class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue = deque([root])
        root.val = 0

        while queue:
            length, levelSum = len(queue), 0

            for node in queue:
                levelSum += (0 if not node.left else node.left.val) + (0 if not node.right else node.right.val)

            while length:
                node = queue.popleft()
                val = levelSum - (0 if not node.left else node.left.val) - (0 if not node.right else node.right.val)

                if node.left:
                    node.left.val = val
                    queue.append(node.left)

                if node.right:
                    node.right.val = val
                    queue.append(node.right)

                length -= 1
        return root