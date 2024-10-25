class Solution:
    def longestPrefix(self, s: str) -> str:
        i,j = 0, 1
        N = len(s)
        lmp = [0 for i in range(N)]

        while j < N:

            if s[i] == s[j]:
                lmp[j] =  i + 1
                i += 1
                j += 1
            else:
                if i == 0:
                    j += 1
                else:
                    i = lmp[i - 1]  

        print(lmp)

        return s[:lmp[-1]]                  