class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        if maze[entrance[0]][entrance[1]] == "+":
            return -1

        roww, coll = len(maze), len(maze[0])

        def isBound(r, c):
            return 0 <= r < roww and 0 <= c < coll

        def isBorder(r, c):
            return r == 0 or r == roww - 1 or c == 0 or c == coll - 1

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        queue = deque()
        queue.append((entrance[0], entrance[1], 0))
        visited = set()
        visited.add((entrance[0], entrance[1]))  

        while queue:
            row, col, count = queue.popleft()

            if isBorder(row, col) and [row, col] != entrance:
                return count

            for dx, dy in directions:
                new_row, new_col = row + dx, col + dy
                if isBound(new_row, new_col) and maze[new_row][new_col] == "." and (new_row, new_col) not in visited:
                    queue.append((new_row, new_col, count + 1))
                    visited.add((new_row, new_col)) 

        return -1
