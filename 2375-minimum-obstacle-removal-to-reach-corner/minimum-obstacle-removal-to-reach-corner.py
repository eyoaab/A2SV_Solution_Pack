class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        distance = [[float('inf')] * n for _ in range(m)]
        deque = collections.deque()

        distance[0][0] = 0
        deque.appendleft((0, 0))
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def inbound(nx,ny):
            return  0 <= nx < m and 0 <= ny < n
        while deque:
            x, y = deque.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if inbound(nx,ny):
                    newDist = distance[x][y] + grid[nx][ny]
                    if newDist < distance[nx][ny]:
                        distance[nx][ny] = newDist
                        if grid[nx][ny] == 0:
                            deque.appendleft((nx, ny))
                        else:
                            deque.append((nx, ny))

        return distance[m-1][n-1]