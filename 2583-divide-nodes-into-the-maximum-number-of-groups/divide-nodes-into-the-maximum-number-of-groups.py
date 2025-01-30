class Solution:

    def magnificentSets(self, n, edges):
        adj_list = [[] for _ in range(n)]
        for edge in edges:
            adj_list[edge[0] - 1].append(edge[1] - 1)
            adj_list[edge[1] - 1].append(edge[0] - 1)

        colors = [-1] * n

        for node in range(n):
            if colors[node] != -1:
                continue
            colors[node] = 0
            if not self._is_bipartite(adj_list, node, colors):
                return -1

        distances = [
            self.bfs(adj_list, node, n)
            for node in range(n)
        ]

        max_number_of_groups = 0
        visited = [False] * n
        for node in range(n):
            if visited[node]:
                continue
            max_number_of_groups += self.helper(
                adj_list, node, distances, visited
            )

        return max_number_of_groups

    def _is_bipartite(self, adj_list, node, colors):
        for neighbor in adj_list[node]:
            if colors[neighbor] == colors[node]:
                return False
            if colors[neighbor] != -1:
                continue
            colors[neighbor] = (colors[node] + 1) % 2
            if not self._is_bipartite(adj_list, neighbor, colors):
                return False
        return True

    def bfs(self, adj_list, src_node, n):
        nodes_queue = deque([src_node])
        visited = [False] * n
        visited[src_node] = True
        distance = 0

        while nodes_queue:
            for _ in range(len(nodes_queue)):
                current_node = nodes_queue.popleft()
                for neighbor in adj_list[current_node]:
                    if visited[neighbor]:
                        continue
                    visited[neighbor] = True
                    nodes_queue.append(neighbor)
            distance += 1

        return distance

    def helper(
        self, adj_list, node, distances, visited
    ):
        max_number_of_groups = distances[node]
        visited[node] = True

        for neighbor in adj_list[node]:
            if visited[neighbor]:
                continue
            max_number_of_groups = max(
                max_number_of_groups,
                self.helper(
                    adj_list, neighbor, distances, visited
                ),
            )
        return max_number_of_groups