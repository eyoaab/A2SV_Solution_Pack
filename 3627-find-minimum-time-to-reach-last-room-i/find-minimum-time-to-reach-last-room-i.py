class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:

        n, m = len(moveTime), len(moveTime[0])
        dist = [[float('inf')] * m for _ in range(n)]
        dist[0][0] = 0
        heap = [(0, 0, 0)] 
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def inbound(nx,ny):
            return  0 <= nx < n and 0 <= ny < m  

        while heap:
            time, x, y = heappop(heap)
            if (x, y) == (n - 1, m - 1):
                return time
            if time > dist[x][y]:
                continue

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                
                if inbound(nx,ny):
                    wait_time = max(time, moveTime[nx][ny])
                    arrival_time = wait_time + 1
                    if arrival_time < dist[nx][ny]:
                        dist[nx][ny] = arrival_time
                        heappush(heap, (arrival_time, nx, ny))
        return -1
