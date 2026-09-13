class Solution:
    def largestOverlap(self, img1, img2):
        n = len(img1)
        best = 0

        for dx in range(-n + 1, n):
            for dy in range(-n + 1, n):
                score = 0
                for i in range(n):
                    for j in range(n):
                        c = 0
                        if 0 <= dx + i < n and 0 <= dy + j < n:
                            c = img1[dx + i][dy + j]
                        score += img2[i][j] & c
                best = max(best, score)

        return best