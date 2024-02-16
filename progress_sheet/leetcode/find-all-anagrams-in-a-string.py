from collections import defaultdict


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        li=[]
        pd=defaultdict(int)
        for k in p:
            pd[k]+=1
        sd=defaultdict(int)
        i=0
        j=0
        while(j<len(s)):
            sd[s[j]]+=1
            if j-i+1==len(p):
                if(sd==pd):
                    li.append(i)
                sd[s[i]]-=1
                if sd[s[i]]==0:
                    del sd[s[i]]
                i+=1
            j+=1
        return li    



         
        
        
         


        



        

    
   
    
