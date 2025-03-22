class UnionFind:
    def __init__(self, n):
        self.parents = {i: i for i in range(n)}
        self.size = [1] * n 

    def find(self, node):
        if self.parents[node] != node:
            self.parents[node] = self.find(self.parents[node]) 
        return self.parents[node]

    def union(self, node1, node2):
        root1, root2 = self.find(node1), self.find(node2)

        if root1 != root2: 
            if self.size[root1] > self.size[root2]:
                self.parents[root2] = root1
                self.size[root1] += self.size[root2]
            else:
                self.parents[root1] = root2
                self.size[root2] += self.size[root1]

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)

        for node1, node2 in edges:
            uf.union(node1, node2)

        vertices = {}
        _edges = {}
        
        for i in range(n):
            root = uf.find(i)
            if root not in vertices:
                vertices[root] = set()
                _edges[root] = 0
            vertices[root].add(i)
        
        for u, v in edges:
            root = uf.find(u)
            _edges[root] += 1
        
        ans = 0
        for root in vertices:
            length = len(vertices[root])

            need = length * (length - 1) // 2
            
            ans += _edges[root] == need
        
        return ans