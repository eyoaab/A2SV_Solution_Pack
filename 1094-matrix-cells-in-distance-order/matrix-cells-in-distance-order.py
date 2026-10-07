class Solution:
    def allCellsDistOrder(
        self,rows: int, cols: int, rCenter: int, cCenter: int ) -> list[list[int]]:

        cells = []

        for r in range(rows):
            for c in range(cols):
                distance = abs(r - rCenter) + abs(c - cCenter)
                cells.append((distance, r, c))

        cells.sort()

        return [[r, c] for distance, r, c in cells]