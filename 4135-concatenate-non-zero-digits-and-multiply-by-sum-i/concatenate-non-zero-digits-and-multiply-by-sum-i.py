class Solution:
    def sumAndMultiply(self, n: int) -> int:
        x = ""
        sum_ = 0

        for s in str(n):
            if s != '0':
                x += s
                sum_ += int(s)

        if len(x) == 0:
            x = "0"

        return int(x) * sum_             

