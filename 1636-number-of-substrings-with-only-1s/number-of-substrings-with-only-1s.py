class Solution:
    def numSub(self, s: str) -> int:
        start = -1
        i = 0
        result = 0
        MOD = 10 ** 9 + 7
        
        while i < len(s):
            if s[i] == '1':
                result = (result + i - start) % MOD
            elif s[i] == '0':
                start = i
            i += 1
        return result

        