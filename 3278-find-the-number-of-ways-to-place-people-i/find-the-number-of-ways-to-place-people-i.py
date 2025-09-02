class Solution:
    def numberOfPairs(self, points: list[list[int]]) -> int:
        points.sort(key=lambda x: (x[0], -x[1]))
        n = len(points)
        ans = 0

        for i in range(n):
            
            top = points[i][1]
            bot = float("-inf")
            for j in range(i + 1, n):
                y = points[j][1]
                if bot < y <= top:
                    ans += 1
                    bot = y
                    if bot == top:
                        break
        return ans