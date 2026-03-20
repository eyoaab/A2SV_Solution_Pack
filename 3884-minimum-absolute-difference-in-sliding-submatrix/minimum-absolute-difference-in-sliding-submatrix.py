class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        return  [
            [0  if len(slide) <= 1 else min(abs(b - a) for a,b in pairwise(sorted(slide)))
                for j in range(len(grid[0]) - k + 1)
                for slide in [set(chain.from_iterable(row[j:j + k] for row in grid[i:i + k]))]
            ]
            for i in range(len(grid) -k + 1)
        ]
        