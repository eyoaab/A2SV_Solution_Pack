class UnionFind:

    def __init__(self, n: int):
        self.parent = {i: i for i in range(n)}
        self.size = {i: 1 for i in range(n)}

    def find(self, x: int) -> int:
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int) -> None:
        root_of_x = self.find(x)
        root_of_y = self.find(y)

        if root_of_x == root_of_y:
            return

        if self.size[root_of_x] >= self.size[root_of_y]:
            self.parent[root_of_y] = root_of_x
            self.size[root_of_x] += self.size[root_of_y]
        else:
            self.parent[root_of_x] = root_of_y
            self.size[root_of_y] += self.size[root_of_x]


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
     
        N = len(isConnected)
        store = UnionFind(N)

        for i in range(N):
            for j in range(i + 1, N):
                if isConnected[i][j]:
                    store.union(i, j)

        return sum(store.find(i) == i for i in range(N))