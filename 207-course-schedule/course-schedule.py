class Solution:
    def canFinish(self, n: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for i in range(n)]
        answer = 0
        indegree = [0 for i in range(n)]
        
        for course,prerequisite in prerequisites:
            indegree[course] += 1
            graph[prerequisite].append(course)

        queue = deque()

        for i in range(n):
            if indegree[i] == 0:
                queue.append(i)

        while queue:
            current = queue.popleft()
            answer += 1

            for  neg in graph[current]:
                indegree[neg] -= 1

                if indegree[neg] == 0:
                    queue.append(neg)

        return answer == n            

                  