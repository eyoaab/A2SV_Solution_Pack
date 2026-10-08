class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        count = 0
        ans = []

        for char in s:
            
            if char is "(":
                if count:
                    ans.append(char)

                count += 1
            else:
                count -= 1
                if count:
                    ans.append(char)





        return "".join(ans)