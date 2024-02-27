class Solution:
    def helper(self, x: float, n: int) -> float:
        if n==0:
            return 1
        elif n == 1:
            return x
        elif n%2 == 0:
            return self.helper(x*x,n//2)
        else:
            return x*self.helper(x*x,n//2)

    def myPow(self, base: float, power: int) -> float:
        if power<0:
            power=power*(-1)
            num=self.helper(base,power)
            return 1/num
        num=self.helper(base,power)
        return num    
        