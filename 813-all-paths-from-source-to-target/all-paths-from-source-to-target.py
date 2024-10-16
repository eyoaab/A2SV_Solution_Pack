class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        paths = []
        def traverse(node, current_path):
            if node == len(graph) - 1:
                paths.append(current_path[:])

            for neighbour in graph[node]:
                current_path.append(neighbour)
                traverse(neighbour, current_path)
                current_path.pop()

        traverse(0, [0])

        return paths


