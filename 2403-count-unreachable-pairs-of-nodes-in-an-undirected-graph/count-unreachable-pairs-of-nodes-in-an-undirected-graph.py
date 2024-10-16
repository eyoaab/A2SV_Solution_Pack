class Solution:
    class UF:
        def __init__(self, size):
            self.parent = list(range(size))  
            self.rank = [0] * size      

        def find(self, x):
            if self.parent[x] != x:
                self.parent[x] = self.find(self.parent[x])
            return self.parent[x]

        def union(self, x, y):
            rootX = self.find(x)
            rootY = self.find(y)

            if rootX != rootY:
                if self.rank[rootX] > self.rank[rootY]:
                    self.parent[rootY] = rootX
                elif self.rank[rootX] < self.rank[rootY]:
                    self.parent[rootX] = rootY
                else:
                    self.parent[rootY] = rootX
                    self.rank[rootX] += 1

        def connected(self, x, y):
            return self.find(x) == self.find(y)

    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        uf = self.UF(n)

        for u, v in edges:
            uf.union(u, v)

        component_size = [0] * n
        for i in range(n):
            root = uf.find(i)
            component_size[root] += 1

        total_pairs = n * (n - 1) // 2  
        connected_pairs = 0
        for size in component_size:
            if size > 1:
                connected_pairs += size * (size - 1) // 2

        return total_pairs - connected_pairs
