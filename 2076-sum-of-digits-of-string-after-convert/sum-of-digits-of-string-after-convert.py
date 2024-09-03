class Solution:
    def getLucky(self, s: str, k: int) -> int:
        transformed = ""

        for i in s:
            alpha = ord(i) - ord('a') + 1
            transformed += str(alpha)

        for i in range(k):
            temp = 0
            for j in str(transformed):
                temp += int(j)

            transformed = str(temp)

        return int(transformed)           

        