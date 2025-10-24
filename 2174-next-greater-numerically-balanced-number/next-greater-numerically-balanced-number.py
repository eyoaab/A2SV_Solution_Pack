class Solution:
    def solve(self, x: int) -> bool:
        s = str(x)
        vec = [0] * 10
        for ch in s:
            vec[ord(ch) - 48] += 1
        for ch in s:
            c = ord(ch)-48
            if c == 0 or vec[c] != c:
                return False
        return True

    def nextBeautifulNumber(self, n: int) -> int:
        i = n + 1
        while True:
            if self.solve(i):
                return i
            i += 1