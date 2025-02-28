class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = defaultdict(lambda : [])
        
        for a, b in connections:
            graph[a].append([b, 1])
            graph[b].append([a, 0]) 
                    
        def dfs(node, prev_node=None, ans = 0):                
            for next_node, direction in graph[node]:
                if next_node == prev_node:
                    continue                
                ans += direction + dfs(next_node, node)
                                
            return ans

        return dfs(0)
        