class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
       
        strs=sorted(strs)

        fir=strs[0]
        sec=strs[-1]
        a=""

        for i in range(min(len(fir),len(sec))):
            if(fir[i]!=sec[i]):
                return str(a)
            a+=fir[i]  
        return a   


