class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dicta=defaultdict(int)
        for i in s1:
            dicta[i]+=1
        dictb=defaultdict(int)
        st=0
        for end in range(len(s2)):
            dictb[s2[end]]+=1
            if (end-st+1==len(s1)):
                if dictb==dicta:
                    return True
                else:
                    dictb[s2[st]]-=1
                    if dictb[s2[st]]==0:
                        del dictb[s2[st]]
                    st+=1
        return False                        

        