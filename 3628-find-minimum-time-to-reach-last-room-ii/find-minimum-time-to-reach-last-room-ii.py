class Solution:
    def minTimeToReach(self, t: List[List[int]]) -> int:
        n, m = len(t), len(t[0])
        dp = [[[float('inf')] * 2 for _ in range(m)] for _ in range(n)]
        dp[0][0][0] = 0

        from heapq import heappush, heappop
        pq = [(0, 0, 0, 0)]  
        directions = [(-1,0), (1,0), (0,-1), (0,1)]

        while pq:
            time, x, y, parity = heappop(pq)
            if dp[x][y][parity] < time:
                continue

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if nx < 0 or ny < 0 or nx >= n or ny >= m:
                    continue

                wait_time = max(time, t[nx][ny])
                next_parity = 1 - parity
                next_time = wait_time + 1 + parity

                if nx == n - 1 and ny == m - 1:
                    return next_time

                if next_time < dp[nx][ny][next_parity]:
                    dp[nx][ny][next_parity] = next_time
                    heappush(pq, (next_time, nx, ny, next_parity))

        return -1