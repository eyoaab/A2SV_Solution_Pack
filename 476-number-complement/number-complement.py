class Solution:
    def findComplement(self, num: int) -> int:
        num = list(bin(num)[2:])
        for i in range(len(num)):
            if num[i] == '0':
                num[i] = '1'
            else:
                num[i] = '0'
        num = int(''.join(num),2) 
        return num       

        