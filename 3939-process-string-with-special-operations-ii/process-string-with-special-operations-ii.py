class Solution:
    def processStr(self, s: str, k: int) -> str:
        n = len(s)

        lengths = [0] * (n + 1)
        curr = 0

        for i, ch in enumerate(s):
            if 'a' <= ch <= 'z':
                curr += 1
            elif ch == '*':
                if curr:
                    curr -= 1
            elif ch == '#':
                curr *= 2
            else:  # %
                pass

            lengths[i + 1] = curr

        if k >= curr:
            return "."

        for i in range(n - 1, -1, -1):
            ch = s[i]

            curr = lengths[i + 1]
            prev = lengths[i]

            if 'a' <= ch <= 'z':
                if k == curr - 1:
                    return ch

            elif ch == '*':
                pass

            elif ch == '#':
                half = prev
                k %= half

            else:  
                k = curr - 1 - k

        return "."