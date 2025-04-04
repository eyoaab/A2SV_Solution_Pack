class Solution(object):
    def lcaDeepestLeaves(self, root):
        def dfs(node, depth):
            if not node:
                return (None, depth)
            
            left_part, left_depth = dfs(node.left, depth + 1)
            right_part, right_depth = dfs(node.right, depth + 1)

            if left_depth > right_depth:
                return (left_part, left_depth)
            elif right_depth > left_depth:
                return (right_part, right_depth)
            else:
                return (node, left_depth)

        lca_node, _ = dfs(root, 0)
        return lca_node