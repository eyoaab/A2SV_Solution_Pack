class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        inDegree = [0 for i in range(numCourses)]
        graph = defaultdict(list)
        order = []

        for node1, node2 in prerequisites:

            inDegree[node1] += 1
            graph[node2].append(node1)

        queue = [index for index,degree in enumerate(inDegree) if degree == 0]

        while queue:
            node = queue.pop()
            order.append(node)

            for neg in graph[node]:
                inDegree[neg] -= 1
                if inDegree[neg] == 0:
                    queue.append(neg)


        return order if len(order) ==  numCourses else []