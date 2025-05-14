#copy
class Solution:
    def lengthAfterTransformations(self, s: str, t: int, nums: List[int]) -> int:
        MOD = 10**9 + 7
        
        transition = [[0] * 26 for _ in range(26)]
        for c in range(26):
            num = nums[c]
            for j in range(1, num + 1):
                next_char = (c + j) % 26
                transition[c][next_char] += 1
        
        def multiply(a, b):
            res = [[0] * 26 for _ in range(26)]
            for i in range(26):
                for k in range(26):
                    if a[i][k] == 0:
                        continue
                    for j in range(26):
                        res[i][j] = (res[i][j] + a[i][k] * b[k][j]) % MOD
            return res
        
        def matrix_pow(mat, power):
            result = [[1 if i == j else 0 for j in range(26)] for i in range(26)]
            while power > 0:
                if power % 2 == 1:
                    result = multiply(result, mat)
                mat = multiply(mat, mat)
                power //= 2
            return result
        
        mat_pow = matrix_pow(transition, t)
        
        cnt = [0] * 26
        for c in s:
            cnt[ord(c) - ord('a')] += 1
        
        new_cnt = [0] * 26
        for i in range(26):
            for j in range(26):
                new_cnt[j] = (new_cnt[j] + cnt[i] * mat_pow[i][j]) % MOD
        
        total = 0
        for x in new_cnt:
            total = (total + x) % MOD
        return total