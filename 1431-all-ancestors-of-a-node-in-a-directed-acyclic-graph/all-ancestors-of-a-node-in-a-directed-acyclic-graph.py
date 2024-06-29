class Solution:
    def getAncestors(self, node_count: int, edges: List[List[int]]) -> List[List[int]]:
        def bfs(node):
            queue = deque([node])
            visited = {node}
            while queue:
                now = queue.popleft()
                for neg in  graph[now]:
                    if neg not in visited:
                        visited.add(neg)
                        ancistor[neg].append(node)
                        queue.append(neg)
        graph = defaultdict(list)
        for node1,node2 in edges:
            graph[node1].append(node2)
        ancistor = [[] for _ in range(node_count)]
        for node in range(node_count):
            bfs(node)
        return ancistor                   
