class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        ans=[]
        for i in image:
            k=i[::-1]
            for j in range(len(k)):
                if k[j]==0:
                    k[j]=1
                else:
                    k[j]=0   
            ans.append(k)  
        return ans           

        