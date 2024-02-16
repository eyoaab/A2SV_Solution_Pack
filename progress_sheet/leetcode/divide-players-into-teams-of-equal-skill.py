class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        r=len(skill)-1
        l=0
        total=0
        sum=skill[l]+skill[r]
        while(l<r):
            if  skill[l]+ skill[r]!=sum:
                return -1
            total+=skill[l]* skill[r]
            l+=1
            r-=1
        return total       