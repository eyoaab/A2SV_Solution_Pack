class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indegree = [0 for i in range(numCourses)]

        for course,preCourse in prerequisites:
            indegree[course] += 1
            graph[preCourse].append(course)

        deque = Deque()

        for index,value in enumerate(indegree):
            if value == 0:
                deque.appendleft(index) 

        answer = []
        visited = set()

        while  deque:
            length =  len(deque)

            for i in range(length):
                node = deque.popleft()
                if not node in visited:
                    visited.add(node)
                    answer.append(node)

                    for child in graph[node]:
                        indegree[child] -= 1
                        if indegree[child] == 0:
                            deque.appendleft(child)

        if len(answer) ==   numCourses:
            return answer

        return []                      

