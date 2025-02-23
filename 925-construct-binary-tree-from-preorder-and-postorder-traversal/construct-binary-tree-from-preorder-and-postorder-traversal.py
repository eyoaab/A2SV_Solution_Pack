class Solution:
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> Optional[TreeNode]:
        index = [0]
        return self.construct(pre, post, index, 0, len(pre) - 1)

    def construct(self, pre, post, index, l, h):
        if index[0] >= len(pre) or l > h:
            return None

        root = TreeNode(pre[index[0]])
        index[0] += 1
        if l == h:
            return root

        i = l
        while i <= h and post[i] != pre[index[0]]:
            i += 1

        if i <= h:
            root.left = self.construct(pre, post, index, l, i)
            root.right = self.construct(pre, post, index, i + 1, h - 1)

        return root