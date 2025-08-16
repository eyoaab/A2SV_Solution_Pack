class Solution:
    def maximum69Number (self, num: int) -> int:
        index = -1

        for i,n in enumerate(str(num)):
            if n == '6':
                index = i
                break

        if index == -1:
            return num

        strNum = str(num) 
        strNum =   strNum[:index] + '9' + strNum[index + 1:]
        return int(strNum)           