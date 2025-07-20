class Node:
    def __init__(self):
        self.children = {}
        self.deleted = False

class Solution:
    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
        root = Node()
        
        for path in paths:
            curr = root
            for name in path:
                if name not in curr.children:
                    curr.children[name] = Node()
                curr = curr.children[name]
        
        store = defaultdict(list)
        self._encode(root, store)
        
        for group in store.values():
            if len(group) > 1:
                for node in group:
                    node.deleted = True
        
        result = []
        self._collect(root, [], result)
        return result
    
    def _encode(self, node: Node, store: dict) -> str:
        if not node.children:
            return "()"
        
        parts = []
        for name, child in node.children.items():
            sub = self._encode(child, store)
            parts.append(name + sub)
        
        parts.sort()
        sign = "(" + "".join(parts) + ")"
        store[sign].append(node)
        return sign
    
    def _collect(self, node: Node, path: List[str], result: List[List[str]]):
        for name, child in node.children.items():
            if child.deleted:
                continue
            path.append(name)
            result.append(path[:]) 
            self._collect(child, path, result)
            path.pop()
