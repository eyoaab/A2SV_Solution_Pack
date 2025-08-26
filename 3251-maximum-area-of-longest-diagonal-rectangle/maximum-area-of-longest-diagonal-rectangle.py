class Solution:
    def areaOfMaxDiagonal(self, dimensions: list[list[int]]) -> int:
        ans, max_diag = 0, 0

        for l, w in dimensions:
            curr = l * l + w * w
            if curr > max_diag or (curr == max_diag and l * w > ans):
                max_diag = curr
                ans = l * w

        return ans