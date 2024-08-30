class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        answer = ''
        N = len(s)

        for i in range(N):
            minChar = min(s[i],s[N - i  - 1])
            answer += minChar


        return answer      