class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        if n == 0:
            return []
                 
        graph = [[] for i in range(n)]
        inDeg = [0 for i in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            inDeg[v] += 1
            inDeg[u] += 1

        queue = deque()
        queue.extend([i for i in range(n) if inDeg[i] == 1])
        Final = deque()
        while queue:
            n = len(queue)
            Final = [node for node in queue]
            for i in range(n):
                node = queue.popleft()
                for neg in graph[node]:
                    inDeg[neg] -= 1
                    if inDeg[neg] == 1:
                        queue.append(neg)
        return Final
            
        