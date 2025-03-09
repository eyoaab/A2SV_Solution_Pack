class Solution:
    def numberOfAlternatingGroups(self, colors, k):
        window = 1
        ans = 0
        n = len(colors)
        for i in range(1, n + k - 2 + 1):
            if colors[i % n] != colors[(i - 1 + n) % n]:
                window += 1
            else:
                window = 1
            if window >= k:
                ans += 1
                
        return ans