class Solution:
    def createBinaryTree(self, descriptions: list[list[int]]) -> Optional[TreeNode]:
        def build_tree(curr):
            new_ = TreeNode(curr)
            if curr in store:
                if store[curr][0] is not None:
                    new_.left = build_tree(store[curr][0])

                if store[curr][1] is not None:
                    new_.right = build_tree(store[curr][1])
                    
            return new_

        childrens = set()
        store: dict[int, list[int]] = {}

        for parent, child, isleft in descriptions:
            if not parent in store:
                store[parent] = [None, None] 
            childrens.add(child)
            target = 0 if isleft else 1
            store[parent][target] = child

        for parent in store:
            if parent not in childrens:
                head_val = parent
                break
        head = build_tree(head_val)

        return head