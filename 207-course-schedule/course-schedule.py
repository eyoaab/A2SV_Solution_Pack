class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        inDegree = [0 for i in range(numCourses)]
        graph = defaultdict(list) #prerequest to 
        visited = set()

        for node1, node2 in prerequisites:
            inDegree[node1] += 1
            graph[node2].append(node1)

        queue = [i for i,degree in enumerate(inDegree) if degree == 0 ]  

        while queue: 
            node = queue.pop()
            visited.add(node)

            for neg in graph[node]:
                inDegree[neg] -= 1
                if inDegree[neg] == 0:
                    queue.append(neg)
                    




        return len(visited) == numCourses