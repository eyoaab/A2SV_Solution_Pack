class Solution:
    def largestGoodInteger(self, num: str) -> str:
        _max=[]
        l=0
        cur=1
        for i in range(1,len(num)):
            if num[i]==num[i-1]:
                cur+=1
                if cur==3:
                    _max.append(int(num[i]))
                    print(_max)
            else:
                cur=1 

        return str(max(_max))*3 if _max else ""               
                           