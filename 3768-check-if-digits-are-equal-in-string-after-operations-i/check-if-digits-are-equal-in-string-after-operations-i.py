class Solution:
    def hasSameDigits(self, s: str) -> bool:
        while len(s) >= 2:
            if len(s) == 2:
                if s[0] == s[1]:
                    return True
                else:
                    return False

            else:
                new = ""
                for i in range(1,len(s)):
                    num1,num2 =  int(s[i]), int(s[i - 1])
                    rem = (num1 + num2) % 10
                    new += str(rem)

                s = new    






        return False                

