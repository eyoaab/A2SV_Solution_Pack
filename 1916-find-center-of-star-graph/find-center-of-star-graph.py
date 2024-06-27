class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        max_ =0
        for node in edges:
            max_ = max(max_,max(node))
        inDegree = [0 for i in range(max_ + 1)]

        for node1,node2 in edges:
            inDegree[node1] += 1
            inDegree[node2] += 1

        return inDegree.index(max(inDegree))  

        