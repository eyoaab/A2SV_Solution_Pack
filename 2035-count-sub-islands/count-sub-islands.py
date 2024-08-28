class Solution:
	def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
		queue, row, col, visited = deque([]),len(grid1), len(grid1[0]), set([])
		count = 0
		for x in range(row):
			for y in range(col):
				if grid1[x][y] == 1 and grid2[x][y] == 1:
					grid2[x][y] = "X"
					queue.append((x,y))
					count += self.subCheck(queue,row,col,visited,grid1,grid2)   
		return count

	def subCheck(self,queue, row, col, visited, grid1, grid2):
		key = True
		while queue:
			x,y = queue.popleft()
			for nx,ny in [[x+1,y], [x-1,y], [x,y+1], [x,y-1]]:
				if 0<=nx<row and 0<=ny<col and grid2[nx][ny] == 1:
					if grid1[nx][ny] != 1:
						key = False
					grid2[nx][ny] = "X"
					queue.append((nx,ny))

		if key:
			return 1

		return 0