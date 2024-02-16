class Solution:
    def smallestNumber(self, num: int) -> int:
        sign = 1 if num >= 0 else -1
        temp = None
        
        if sign == 1:
            temp = sorted(str(num))
        else:
            temp = sorted(str(num)[1:], reverse = True)
        
        if temp[0] == '0':
            i = 0
            while i < len(temp) and temp[i] == '0':
                i += 1
            if i < len(temp):
                temp[i], temp[0] = temp[0], temp[i]
        
        return sign*int(''.join(temp))