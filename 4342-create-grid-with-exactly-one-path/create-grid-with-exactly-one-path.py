class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        ans = []
        for i in range(m):
            ans.append('#' * n)

        for i in range(m):
            ans[i] = '.' + ans[i][1:] 

        ans[-1] = '.'  * n

        return ans         