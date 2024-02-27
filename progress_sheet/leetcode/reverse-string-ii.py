class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        ans=''
        li=list()
        for i in s:
            li.append(i)
        p=0
        while(p<len(li)):
            if(len(s)-p)<k:
                ans+=''.join(li[p:][::-1]) 
            else:
                ans+=''.join(li[p:p+k][::-1]) 
            ans+=''.join(li[p+k:p+2*k])     
            p+=2*k
        return ans              