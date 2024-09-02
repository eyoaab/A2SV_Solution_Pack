class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        total = 0
        for i in s:
            if i.isdigit():
                total *= int(i)
            else:
                total += 1

        for i in range(len(s) - 1,-1,-1):
            k  %= total

            if( k == 0 or k == total) and (not s[i].isdigit()):
                return s[i]   

            if s[i].isdigit():
                total //= int(s[i])
            else:
                total -= 1  

        return ''                      

       