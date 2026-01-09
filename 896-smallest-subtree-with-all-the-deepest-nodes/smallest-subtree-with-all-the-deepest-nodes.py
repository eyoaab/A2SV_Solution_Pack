class Solution:
    class Pair:
        def __init__(self, d, n):
            self.depth = d
            self.node = n

    def dfs(self, root):
        if root is None:
            return Solution.Pair(0, None)
        left = self.dfs(root.left)
        right = self.dfs(root.right)

        if left.depth == right.depth:
            return Solution.Pair(left.depth + 1, root)
        elif left.depth > right.depth:
            return Solution.Pair(left.depth + 1, left.node)
        else:
            return Solution.Pair(right.depth + 1, right.node)

    def subtreeWithAllDeepest(self, root):
        return self.dfs(root).node