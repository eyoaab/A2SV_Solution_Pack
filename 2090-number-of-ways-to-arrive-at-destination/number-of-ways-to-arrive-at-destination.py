class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        for u, v, time in roads:
            graph[u].append((v, time))
            graph[v].append((u, time))
            
        dist = [float('inf')] * n
        ways = [0] * n
        
        dist[0] = 0
        ways[0] = 1
        
        heap = [(0, 0)]
        
        MOD = 10**9 + 7
        
        while heap:
            d, node = heappop(heap)
            
            if d > dist[node]:
                continue
                
            for neighbor, time in graph[node]:
                if dist[node] + time < dist[neighbor]:
                    dist[neighbor] = dist[node] + time
                    ways[neighbor] = ways[node]
                    heappush(heap, (dist[neighbor], neighbor))
                    
                elif dist[node] + time == dist[neighbor]:
                    ways[neighbor] = (ways[neighbor] + ways[node]) % MOD
        
        return ways[n-1]