class Solution:
    def isBalanced(self, num: str) -> bool:
        sum_ = 0
        isOdd = False
        for s in num:
            if isOdd:
                sum_ -= int(s)
            else:
                sum_ += int(s)  

            isOdd = not isOdd

        return sum_ == 0          

        