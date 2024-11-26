class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        indegree = [0 for i in range(n)]
        
        for node1,node2 in edges:

            indegree[node2] += 1

        possible_answer = []

        for index,val in  enumerate(indegree):
            if not val:
               possible_answer.append(index)

        if len(possible_answer) > 1:
            return -1

        return possible_answer[0]    