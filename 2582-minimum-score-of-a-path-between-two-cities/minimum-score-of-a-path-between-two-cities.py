class UnionFind:
    def __init__(self, size):
        self.parent = {i:i for i in range(size)}
        self.size = {i:1 for i in range(size)}

    def find(self, x):
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]

        return x

    def union(self,x,y):
        repx = self.find(x)
        repy = self.find(y)

        if repx != repy:
            if self.size[repx] > self.size[repy]:
                self.parent[repy] = repx
                self.size[repx] += self.size[repy]
            else:
                self.parent[repx] = repy
                self.size[repy] += self.size[repx]
class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        store = UnionFind(n+1)
        for road in roads:
            store.union(road[0],road[1])
        answer = float('inf')
        for src,des,distan in roads:
            initial = store.find(1)
            source = store.find(src) 
            destination = store.find(des)

            if initial == source == destination:
                answer  = min(answer,distan)

        return answer             


        