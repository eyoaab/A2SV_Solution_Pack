class UnionFind:
    def __init__(self, n):
        self.parent = {i:i for i in range(n + 1)}
        self.size = {i:1 for i in range(n + 1)}
        self.n = n 

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
            self.n -= 1  
            return 1   
        else:
            return 0 
    def isConnected(self):
        return self.n == 1               
class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        Bob = UnionFind(n)
        Alice = UnionFind(n)

        the_minimum = 0
        for flag,node1,node2 in edges:
            if flag == 3:
                the_minimum += Bob.union(node1,node2) |  Alice.union(node1,node2)
                
        for flag,node1,node2 in edges:
            if flag == 2:
                the_minimum +=  Bob.union(node1,node2)
               
            else:
                the_minimum +=  Alice.union(node1,node2)
               

        if Bob.isConnected() and Alice.isConnected():
            return len(edges) - the_minimum
        return -1                    


        
        