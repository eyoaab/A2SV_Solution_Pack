class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        answer = ""
        left = 0
        ones = 0

        for right in range(len(s)):
            if s[right] == '1':
                ones += 1

            while ones > k:
                if s[left] == '1':
                    ones -= 1
                left += 1

            while ones == k and s[left] == '0':
                left += 1

            if ones == k:
                candidate = s[left:right + 1]

                if (
                    not answer
                    or len(candidate) < len(answer)
                    or (len(candidate) == len(answer) and candidate < answer)
                ):
                    answer = candidate

        return answer