class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        referance=defaultdict(list)

        for path in paths:
            temp=path.split()
            root=temp[0]

            for p in temp[1:]:
                temp2=p.split('(')
                referance[temp2[1][:-1]].append(str(root)+'/'+ temp2[0])
                
        #print(referance.items())

        answer=[]
        for i,j in referance.items():
            if len(j)>1:
                answer.append(j)

        return answer                 
        