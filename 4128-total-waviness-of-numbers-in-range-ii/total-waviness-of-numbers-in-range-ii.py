class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:

        num1 = str(num1)
        num2 = str(num2)

        num1 = "0"*(len(num2) - len(num1)) + num1

        @cache
        def dp(i, num_start, tight, tight2, prev, prevprev, val):
            if i == len(num1):
                return val  

            res = 0

            l = int(num2[i]) if tight else 9
            start = 0 if not tight2 else int(num1[i]) 
            num_start = num_start or prevprev > 0
            for j in range(start, l+1):
                newtight = tight and j == int(num2[i])
                newtight2 = tight2 and j == int(num1[i])
    
                add = 0
                if (prevprev != -1 or prev == -1) and num_start:
                    add = 1 if j > prev < prevprev or j < prev > prevprev else 0
                
                res += dp(i+1, num_start, newtight, newtight2, j, prev, val + add)
            return res
        
        return dp(0, False, True, True, -1, -1, 0)
