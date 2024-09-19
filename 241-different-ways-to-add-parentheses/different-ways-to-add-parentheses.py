class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        res = []
        for i in range(len(expression)):
            oper = expression[i]
            if oper == "+" or oper == "-" or oper == "*":
                sub_str1 = expression[0 : i]
                sub_str2 = expression[i + 1 : ]
                left = self.diffWaysToCompute(sub_str1)
                right = self.diffWaysToCompute(sub_str2)
                for i in left:
                    for j in right:
                        if oper == "*":
                            res.append(int(i) * int(j))
                        if oper == "+":
                            res.append(int(i) + int(j))
                        if oper == "-":
                            res.append(int(i) - int(j))
        if len(res) == 0:
            res.append(int(expression))
        return res