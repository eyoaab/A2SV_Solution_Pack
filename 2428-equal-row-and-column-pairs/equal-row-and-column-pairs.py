class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        Cols = defaultdict(list)

        for i in range(len(grid)):
            row = grid[i]

            for index,num in enumerate(row):
                Cols[index].append(num)

        answer = 0  

        for row in  grid:
            answer += list(Cols.values()).count(row)

        return answer             