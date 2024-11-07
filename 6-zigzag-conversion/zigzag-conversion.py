class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        index, d = 0, 1
        rows = [[] for _ in range(numRows)]

        for char in s:
            rows[index].append(char)
            if index == 0:
                d = 1
            elif index == numRows - 1:
                d = -1
            index += d

        for i in range(numRows):
            rows[i] = ''.join(rows[i])

        return ''.join(rows)   