class Solution:
    def countCommas(self, n):
        if n <= 999:
            return 0

        totalCommas = 0
        rangeStart = 1000
        rangeEnd = rangeStart * 1000 - 1
        commas = 1

        while rangeStart <= n:
            numbers = min(n, rangeEnd) - rangeStart + 1
            totalCommas += commas * numbers

            if rangeEnd > n:
                break
            rangeStart *= 1000
            rangeEnd = rangeStart * 1000 - 1
            commas += 1

        return totalCommas