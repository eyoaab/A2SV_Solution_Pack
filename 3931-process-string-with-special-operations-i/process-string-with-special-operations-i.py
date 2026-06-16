class Solution:
    def processStr(self, s: str) -> str:
        result = ""

        for letter in s:
            if letter == "*" and len(result)  != 0:
                result = result[:len(result) - 1]
                continue
            elif letter == "#" and len(result) != 0:
                result +=  result
                continue
            elif letter == "%":
                result = result[::-1]
                continue
            elif letter not in "#*%":
                result += letter

        return result                

                