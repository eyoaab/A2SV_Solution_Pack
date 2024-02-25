class Solution:
    def romanToInt(self, s: str) -> int:

        referance={
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000,
            '0':0
        }
        s+='0'
        _sum=0

        for i in range(len(s)-1):
           
            if referance[s[i]]<referance[s[i+1]]:
                _sum-=referance[s[i]]
            else:
                 _sum+=referance[s[i]]    

        return _sum

        