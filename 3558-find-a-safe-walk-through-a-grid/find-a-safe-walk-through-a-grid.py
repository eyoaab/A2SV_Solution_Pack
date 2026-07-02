class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        m, n = len(grid), len(grid[0])

        dist = [[float("inf")] * n for _ in range(m)]

        dq = deque()

        dist[0][0] = grid[0][0]
        dq.appendleft((0, 0))

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while dq:
            x, y = dq.popleft()

            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if not (0 <= nx < m and 0 <= ny < n):
                    continue

                new_cost = dist[x][y] + grid[nx][ny]

                if new_cost < dist[nx][ny]:
                    dist[nx][ny] = new_cost

                    if grid[nx][ny] == 0:
                        dq.appendleft((nx, ny))
                    else:
                        dq.append((nx, ny))

        return dist[m - 1][n - 1] < health