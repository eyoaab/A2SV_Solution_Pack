class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        temp=defaultdict(int)

        for cur in cpdomains:
            first=cur.split()
            n=int(first[0])
            second=list(first[1].split('.'))
            
            #temp[second[-1]]+=n#to give the value
            for j in range(len(second)):
                k='.'.join(second[j:])
                temp[k]+=n  

        answer=[]
        for k,val in temp.items():
            now=str(val)+" "+str(k)
            answer.append(now) 
        
        return answer             
                    

        