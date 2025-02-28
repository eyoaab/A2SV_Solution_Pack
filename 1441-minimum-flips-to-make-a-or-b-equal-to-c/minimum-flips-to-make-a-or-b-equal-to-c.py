class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        def isZero(num,k):
            return num &( 1 << k)  == 0

        ans = 0
        for i in range(32):
            first = isZero(a,i)
            second = isZero(b,i)
            third = isZero(c,i)

            if third:# if third is zero
                # ans += not(first or second)
                if  first and  second:
                    continue
                else:
                    ans += not first
                    ans += not second    


            else:
                if(not first or not second):
                    continue
                else:
                    ans += 1    



        return ans
        