class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        ans = int(dividend/divisor)

        maxans = 2**31-1
        minans = -2**31

        if ans > maxans:
            return maxans 
        elif ans   < minans:
            return minans 
        else :
            return ans  