class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        size = r - l + 1
        pref = [i for i in range(size)]
        mod = 10 ** 9 + 7

        for i in range(n-1):
            new = []
            curr = 0
            for j in range(size - 1,-1,-1):
                new.append(curr)
                curr += pref[j]
                curr %= mod
            pref = new

        return (curr * 2) % mod