class Solution:
    def numSteps(self, s: str) -> int:
        num = int(s,2)
        ans = 0
        
        while(num != 1):
            if(num % 2 == 0):
                num = num // 2
            else:
                num += 1
            ans += 1

        return ans           
        