class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        answer = 0
        prev = 0


        for tax,percent in brackets:
            temp = min(tax,income)

            temp -= prev
            prev =  min(tax,income)

            answer += temp * (percent  / 100)

        return answer    