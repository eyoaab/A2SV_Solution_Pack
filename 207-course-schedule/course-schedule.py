class Solution:
    def canFinish(self, n: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(n)]
        inDegree = [0] * n
        answer = []

        for pair in prerequisites:

            course,prerequisite = pair

            graph[prerequisite].append(course)
            inDegree[course] += 1

        queue = deque()
        for i in range(n):
            if inDegree[i] == 0:
                queue.append(i)

        while queue:
            current = queue.popleft()
            answer.append(current)

            for next_course in graph[current]:
                inDegree[next_course] -= 1
                if inDegree[next_course] == 0:
                    queue.append(next_course)

        return len(answer) == n