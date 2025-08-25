class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        cols, ans = len(encodedText) // rows, ""

        for i in range(cols):
            for j in range(i, len(encodedText), cols + 1):
                ans += encodedText[j]

        return ans.rstrip()     