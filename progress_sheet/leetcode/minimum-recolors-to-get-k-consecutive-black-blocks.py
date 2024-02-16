class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        c= blocks[0:k].count('W')
        i=0
        j=k-1
        while(j< len(blocks)):
            c=min(c,blocks[i:j+1].count('W'))
            i+=1
            j+=1
        return c    
        