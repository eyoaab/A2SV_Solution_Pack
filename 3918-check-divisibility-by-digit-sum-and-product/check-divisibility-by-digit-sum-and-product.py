class Solution:
    def checkDivisibility(self, n: int) -> bool:
        digitSum = 0
        digitProd = 1
        sum_ = 0

        for char in str(n):
            digitSum += int(char)
            digitProd *= int(char)

        sum_ += digitSum + digitProd    

        if not sum_:
            return False

        return n % sum_ == 0         