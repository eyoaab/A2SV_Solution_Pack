class Solution:
    def minimumBoxes(self, a, c):
        ans = 0
        s = sum(a)
        c.sort()

        i = len(c) - 1
        while i >= 0:
            s -= c[i]
            ans += 1
            if s <= 0:
                break
            i -= 1

        return ans
