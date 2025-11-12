class Solution:
    def minOperations(self, a):
        n = len(a)
        all_e = all(x % 2 == 0 for x in a)
        has_o = any(x == 1 for x in a)

        if all_e:
            return -1
        if has_o:
            return n - a.count(1)

        mn = n + 1
        for i in range(n):
            gc = 0
            for j in range(i, n):
                gc = gcd(gc, a[j])
                if gc == 1:
                    mn = min(mn, j - i + 1)
                    break
        return -1 if mn == n + 1 else mn + n - 2