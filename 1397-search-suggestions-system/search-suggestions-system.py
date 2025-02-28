class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
        self.suggestions = []

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        root = self.build_trie(products)
        res = []
        node = root
        for char in searchWord:
            if char in node.children:
                node = node.children[char]
                res.append(node.suggestions)
            else:
                node = TrieNode()
                res.append([])
        return res

    def build_trie(self, products):
        root = TrieNode()
        for product in products:
            node = root
            for char in product:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
                if len(node.suggestions) < 3:
                    node.suggestions.append(product)
            node.is_end = True
        return root
        